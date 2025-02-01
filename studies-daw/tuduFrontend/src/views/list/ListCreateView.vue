<template>
    <v-container>
      
      <v-row>
        <v-col>
          <h1>Listas</h1>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6" md="4" lg="3">

          <v-sheet>
            <v-form ref="form" @submit.prevent="addList">
              <v-text-field
                v-model="newList.title"
                :counter="40"
                :rules="newList.nameRules"
                label="Nombre de la lista"
              ></v-text-field>
              <v-btn
                color="primary"
                type="submit"
              >Agregar lista</v-btn>
              <v-list>
                <v-list-item
                  v-for="(list, index) in listList"
                  :key="index"
                >
                  <div>
                    <h4>{{ list.title }}</h4>
                  </div>
                </v-list-item>
              </v-list>
            </v-form>
          </v-sheet>

        </v-col>
      </v-row>

    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    data: () => ({
      newList: {
        title: "",
        nameRules: [
          (v) => !!v || "El nombre es requerido",
          (v) => (v && v.length <= 40) || "El nombre debe tener menos de 40 caracteres",
        ],
        user: localStorage.getItem("user_id"),
      },
      listList: [],
      urlUser : 'http://127.0.0.1:8000/api/v1/users/',
      urlCreateList: 'http://127.0.0.1:8000/api/v1/lists/create/'
    }),
    mounted() {
      this.getLists();
    },
    methods: {
      getLists() {
        const userId = this.newList.user;
        axios
          .get(this.urlUser + userId + '/lists/')
          .then((response) => {
            this.listList = response.data;
          })
          .catch((error) => {
            console.error(error.response);
          });
      },
      addList() {
        if (this.newList.title){
          var data = {
            title: this.newList.title,
            user_id: parseInt(this.newList.user),
          };
          console.log('Data: ', data);
          axios
            .post(this.urlCreateList, data)
            .then((response) => {
              console.log('Response: ', response);
              this.getLists();
              this.newList.title = "";
              this.$router.push('/mylists');
            })
            .catch((error) => {
              console.log('Error: ', error);
              console.log('Error creando la lista');

            });

        }
      },
    }
  };
  </script>
  <style lang="sass" src="@/assets/sass/pages/lists/_listCreate.sass" scoped></style>
  ```