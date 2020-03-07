import axios from 'axios'
let base = '';

export const POST = (url, params) => {
  return axios.post(`${base}${url}`, params)
}

export const GET = (url, params) => {
  return axios.get(`${base}${url}`, {params:params})
}

export const PUT = (url, params) => {
  return axios.put(`${base}${url}`, params)
}

export const DELETE = (url, params) => {
  return axios.delete(`${base}${url}`, {data:params})
}

