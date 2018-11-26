const isItemInList = (item, list) =>
  list.map(el => el.id).includes(item.id);


const addItemToList = (item, list) =>
  [...list, item];


const updateItemInList = (item, list) =>
  list.map(el => (el.id === item.id ? item : el));


// Update the state for error data
const error = {
  WRITE_ERROR: (state, action) => ({
    ...state,
    error: {
      ...state.error,
      errors: action.errors,
    },
  }),
  SHOW_ERROR: state => ({
    ...state,
    error: {
      ...state.error,
      visible: true,
    },
  }),
  CLEAR_ERROR: state => ({
    ...state,
    // Set all data items to 'not loading'
    data: Object.entries(state.data)
      .map(([key, data]) => [key, { ...data, loading: false }])
      .reduce((obj, [key, data]) => { obj[key] = data; return obj; }, {}),
    error: {
      ...state.error,
      errors: null,
      visible: false,
    },
  }),
};


const buildNewQuestion = id => ({
  id: id,
  prompt: '',
  type: '',
  options: [],
  follows: [],
  start: false,
})


const question = {
  CREATE_QUESTION: (state, action) => ({
    ...state,
    script: {
      ...state.script,
      [action.id]: buildNewQuestion(action.id)
    },
  }),
  UPDATE_QUESTION: (state, action) => {
    return {
      ...state,
      script: { ...state.script, [action.question.id]: action.question },
    }
  },
  REMOVE_QUESTION: (state, action) => {
    const script = { ...state.script }
    delete script[action.id]
    return {
      ...state,
      script: script,
    }
  },
  ADD_FOLLOWS: (state, action) => {
    const question = state.script[action.id]
    return {
      ...state,
      script: {
        ...state.script,
        [question.id]: {
          ...question,
          follows: [
            ...question.follows,
            {
              id: action.prev,
              when: action.when ? { id: action.when, value: action.value} : null,
            },
          ]
        }
      }
    }
  },
  REMOVE_FOLLOWS: (state, action) => {
    const follows = action.follows
    const question = { ...state.script[action.id] }
    question.follows = question.follows
      .filter(f => {
        // Filter out the follows that we want to remove
        const isMatchPrevId = f.id === follows.id
        const isMatchWhen = (
          (!f.when && !follows.when) ||
          f.when && follows.when &&
          f.when.id === follows.when.id &&
          f.when.value === follows.when.value
        )
        return !(isMatchPrevId && isMatchWhen)
      })

    return {
      ...state,
      script: { ...state.script, [question.id]: question },
    }
  },
}


// Generic operations on backend API data
const generic = {
  // Update or insert a single data item, based on id
  UPSERT_ITEM: (state, action) => ({
    ...state,
    data: {
      ...state.data,
      [action.key]: {
        ...state.data[action.key],
        loading: action.loading || false,
        lookup: { ...state.data[action.key].lookup, [action.item.id]: action.item },
        list: isItemInList(action.item, state.data[action.key].list) ?
          updateItemInList(action.item, state.data[action.key].list) :
          addItemToList(action.item, state.data[action.key].list),
      },
    },
  }),
  // Mark a set of data items as "loading"
  SET_LOADING: (state, action) => ({
    ...state,
    data: {
      ...state.data,
      [action.key]: {
        ...state.data[action.key],
        loading: true,
      },
    },
  }),
  // Mark a set of data items as not "loading"
  UNSET_LOADING: (state, action) => ({
    ...state,
    data: {
      ...state.data,
      [action.key]: {
        ...state.data[action.key],
        loading: false,
      },
    },
  }),
  // Received a set of data items from the backend
  RECEIVE_LIST: (state, action) => ({
    ...state,
    data: {
      ...state.data,
      [action.key]: {
        loading: false,
        list: action.data,
        lookup: action.data.reduce((obj, el) => { obj[el.id] = el; return obj; }, {}),
      },
    },
  }),
}


// Combine all our reducers into a single reducer lookup table.
const reducer = {
  ...question,
  ...error,
  ...generic,
}


// The final reducer function, which we pass to Redux.
export default (state, action) => {
  const func = reducer[action.type]
  if (!func) return { ...state }
  return func(state, action)
}
