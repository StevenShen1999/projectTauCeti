import axios from 'axios'
import qs from 'qs'

export default {
    namespaced: true,
    state: {
        token: localStorage.getItem('token') || '',
        status: ''
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status

    }, 
    mutations: {

        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token, user){
            state.status = 'success'
            state.token = token
            state.user = user
        },
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = ''
            state.token = ''
        },
    },
    actions: {
        login({commit}, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({
                    url: 'auth/login',
                    data: user,
                    method: 'POST'
                })
                .then(r=> {
                    const token = r.data.token
                    const user = r.data.user
                    localStorage.setItem('token',token)
                    commit('auth_success', token, user)
                    resolve(r)
                })
                .catch(e => {
                    commit('auth_error')
                    localStorage.removeItem('token')
                    reject(e)
                })
            })
        },
        register({ commit }, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({
                    url: 'auth/register',
                    data: qs.stringify(user),
                    method: 'POST'
                })
                .then(r=> {
                    const token = r.data.token
                    const user = r.data.user
                    localStorage.setItem('token',token)
                    commit('auth_success', token, user)
                    resolve(r)
                })
                .catch(e => {
                    commit('auth_error')
                    localStorage.removeItem('token')
                    reject(e)
                })
            })
        },
        logout({commit}) {
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('token')
                resolve()
            })
        }

    }
}