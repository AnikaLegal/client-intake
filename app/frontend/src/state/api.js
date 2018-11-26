import Cookies from 'universal-cookie'

import urls from 'urls'

const getCSRF = () => new Cookies().get('csrftoken')

// POST a JSON to url
const post = (url, data) =>
  fetch(url, {
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: {
      'X-CSRFToken': getCSRF(),
      'Content-Type': 'application/json',
    },
  })

// GET a url
const get = url => fetch(url, { credentials: 'include' })

// All HTTP API calls made by the frontend
export default {
  script: {
    // List all scripts
    list: () => get(urls.api.script.list()),
  },
  question: {
    // List all questions
    list: () => get(urls.api.question.list()),
  },
}
