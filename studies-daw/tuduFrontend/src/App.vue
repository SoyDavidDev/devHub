<template>
  <v-app>
    <v-app-bar>
      <v-toolbar-title style="margin-top: 3rem;">
        <!-- <BasicImage
        :src="imageBrand.header.icon.src"
        :alt="imageBrand.header.icon.alt"
        :isIcon="imageBrand.header.icon.isIcon"
        :width="imageBrand.header.icon.width"
        :height="imageBrand.header.icon.height"
        class="icon1"
        /> -->
        <BasicImage
        :src="imageBrand.header.icon2.src"
        :alt="imageBrand.header.icon2.alt"
        :isIcon="imageBrand.header.icon2.isIcon"
        :width="imageBrand.header.icon2.width"
        :height="imageBrand.header.icon2.height"
        class="icon2"
        />
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/">Home</v-btn>
      <v-btn text to="/about">About</v-btn>
      <v-btn text to="/login"
      v-if="!isLoggedIn">Login</v-btn>
      <v-btn text to="/register"
      v-if="!isLoggedIn">Register</v-btn>
      <v-btn text to="/mylists"
      v-if="isLoggedIn">My Lists</v-btn>
      <v-btn text to="/profile"
      v-if="isLoggedIn">Profile</v-btn>
      <v-btn text to="/login" @click="logout"
      v-if="isLoggedIn">Logout</v-btn>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import BasicImage from '@/components/basic/image/index.vue'
import auth from "@/services/auth.js";
import { computed , onMounted } from 'vue';
import { useMeta } from 'vue-meta';
import { useStore } from "vuex";

export default {
  name: "App",
  components: {
    BasicImage,
  },
  created(){
    setInterval(() => {
      auth.refreshToken();
    }, 1800000);
  },
  setup(){
    useMeta({
      title: 'Tudus',
    });
  },

  data (){
    return {
      imageBrand: require('@/content/basic/branding/text.js')
    }
  },
  setup(){
    const store = useStore();

    const refreshToken = async () => {
      setInterval(async () => {
        try {
          const response = await auth.refreshToken();
          localStorage.setItem("accessToken", response.access);
          document.cookie = `accessToken=${response.access}; path=/; max-age=3600`;
        } catch (error) {
          console.log("Error al refrescar el token");
        }
      }, 60000);
    };

    onMounted(refreshToken);

    return {
      isLoggedIn: computed(() => store.state.isLoggedIn),
      logout: ()=>{
        auth.logout();
        document.cookie = "accessToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        store.commit("setLoggedIn", false);
      }
    }
  }
};
</script>
<style lang="sass" src="@/assets/sass/pages/home/_home.sass" ></style>
