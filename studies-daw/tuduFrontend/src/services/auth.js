import axios from "axios"
import store from '@/store'

const URLToken = 'http://127.0.0.1:8000/api/v1/token/';
const URLCreateUser = 'http://127.0.0.1:8000/api/v1/users/create/';
const URLResetPassword = 'http://127.0.0.1:8000/api/v1/users/reset_password/';
const URLConfirmResetPassword = 'http://127.0.0.1:8000/api/v1/users/reset_password/confirm/';

export default {
  async login(username, password) {
    console.log('login');
    try {
      const response = await axios.post(URLToken, {
        username,
        password,
      });
      
      localStorage.setItem("accessToken", response.data.access);
      localStorage.setItem("refreshToken", response.data.refresh);
      localStorage.setItem("user_id", response.data.id);
      localStorage.setItem('was_inactive', response.data.was_inactive);
      document.cookie = `accessToken=${response.data.access}; path=/; max-age=3600`; 
      return response.data;
    } catch (error) {
      return error.response.data;
    }
  },

  logout() {
    console.log("logout");
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    localStorage.removeItem("user_id");
    store.commit("setLoggedIn", false);
  },

  async register(username, first_name, last_name, email, password) {
    try{
      const response = await axios.post(URLCreateUser, {
        username,
        first_name,
        last_name,
        email,
        password,
      });
      console.log('Register success');
      return response.data;
    } catch (error) {
      console.log(error.response.data);
      console.log('Error in register');
      throw error;
    }
  },



  async refreshToken() {
    const refreshToken = localStorage.getItem("refreshToken");
    if (!refreshToken){
      console.log('No refresh token');
      return;
    } else{
      try{
        const response = await axios.post(URLToken + "refresh/", {
          refresh: localStorage.getItem("refreshToken"),
        });
        localStorage.setItem("accessToken", response.data.access);
        document.cookie = `accessToken=${response.data.access}; path=/; max-age=3600`;
        return response.data;
      } catch (error){
        console.log('Error in refresh token');
        console.log(error);
      }
    }
  },

  async resetPassword(email) {
    console.log('reset password');
    try{
      const response = await axios.post(URLResetPassword, {
        email,
      });
      console.log('Reset password success');
      return response.data;
    } catch (error) {
      console.log(error.response.data);
      console.log('Error in reset password');
      return error.response.data;
    }
  },

  async confirmResetPassword(token, password) {
    try{
      const response = await axios.post(URLConfirmResetPassword, {
        token,
        password,
      });
      return response.data;
    } catch (error) {
      console.log(error.response.data);
      console.log('Error in confirm reset password');
      return error.response.data;
    }
  },

}