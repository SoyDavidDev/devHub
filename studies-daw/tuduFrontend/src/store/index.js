import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

export default createStore({
    state:{
        isLoggedIn: false,
    },
    mutations:{
        setLoggedIn(state, value){
            state.isLoggedIn = value;
        },
    },
    plugins: [createPersistedState()],

});