import uniqid from 'uniqid'

import { api } from 'state'
import { checkForError, handleJSONResponse, handleError } from './utils'

// Generic action to fetch a list of data
const list = (dispatch, dataType, apiCall, ...args) => {
  dispatch({ type: 'SET_LOADING', key: dataType })
  return apiCall(...args)
    .then(handleJSONResponse(dispatch))
    .then(data => dispatch({ type: 'RECEIVE_LIST', key: dataType, data }))
    .catch(handleError(dispatch))
}

// Generic action to upsert a data item
const upsert = (dispatch, dataType, apiCall, ...args) => {
  dispatch({ type: 'SET_LOADING', key: dataType })
  return apiCall(...args)
    .then(handleJSONResponse(dispatch))
    .then(item => dispatch({ type: 'UPSERT_ITEM', key: dataType, item }))
    .catch(handleError(dispatch))
}

// All actions performed by the frontend.
export default {
  // Actions affecting error messages
  error: {
    clear: () => ({ type: 'CLEAR_ERROR' }),
  },
  // Actions affecting questionnaire scripts
  script: {
    list: () => dispatch => list(dispatch, 'script', api.script.list),
    create: (...args) => dispatch =>
      upsert(dispatch, 'script', api.script.create, ...args),
    setFirstQuestion: (...args) => dispatch =>
      upsert(dispatch, 'script', api.script.setFirstQuestion, ...args),
  },
  // Actions affecting questions
  question: {
    list: () => dispatch => list(dispatch, 'question', api.question.list),
    create: (...args) => dispatch =>
      upsert(dispatch, 'question', api.question.create, ...args),
    update: (...args) => dispatch =>
      upsert(dispatch, 'question', api.question.update, ...args),
  },
  // Actions affecting transitions
  transition: {
    create: dispatch => (...args) => {
      dispatch({ type: 'SET_LOADING', key: 'question' })
      return (
        api.transition
          .create(...args)
          .then(handleJSONResponse(dispatch))
          // We get a question back as a response, rather than just the transition.
          .then(item =>
            dispatch({ type: 'UPSERT_ITEM', key: 'question', item })
          )
          .catch(handleError(dispatch))
      )
    },
  },
}
