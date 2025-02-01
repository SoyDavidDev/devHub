<template>
  <div class="profile-view">
    <h1 class="title">Gestión de perfil</h1>
    <form action class="form" @submit.prevent="updateProfile">

        <div class="form-passwordChanging" v-if="passwordChange">
          <label for="password" class="form-label">Contraseña Actual:</label>
          <v-text-field 
            label="Contraseña Actual" 
            :type="show1 ? 'text' : 'password'" 
            id="password"
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show1 = !show1"
          />
          <label for="new_password" class="form-label">Nueva Contraseña:</label>
          <v-text-field 
            label="Nueva Contraseña" 
            :type="show2 ? 'text' : 'password'" 
            id="new_password"
            v-model="new_password"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show2 = !show2"
          />
          <label for="new_password_repeat" class="form-label">Repetir Nueva Contraseña:</label> 
          <v-text-field 
            label="Repetir Nueva Contraseña" 
            :type="show3 ? 'text' : 'password'" 
            id="new_password_repeat"
            v-model="new_password_repeat"
            :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show3 = !show3"
          />
        </div>

        <div class="form-container" v-if="!passwordChange">
          <label for="username" class="form-label">Nombre de usuario:</label>
          <v-text-field label="Nombre de usuario" v-model="username" />
          <label for="first_name" class="form-label">Nombre:</label>
          <v-text-field label="Nombre" v-model="first_name" />
          <label for="last_name" class="form-label">Apellidos:</label>
          <v-text-field label="Apellidos" v-model="last_name" />
          <label for="email" class="form-label">Email:</label>
          <v-text-field label="Email" v-model="email" />
        </div>

              
        <div class="form-actions">

          <div class="form-actions-messages">
            <p class="error" v-if="!updatedMessage">
              {{errorMessage}}
            </p>
          </div>
          <div class="form-actions-messages">
            <p class="updated" v-if="!errorMessage">
              {{updatedMessage}}
            </p>
          </div>
          <input 
            class="form-submit" 
            type="submit" 
            :value="passwordChange ? 'Cambiar Contraseña' : 'Actualizar Perfil'"
          >
          <v-card-actions>
            <v-btn 
              color="secondary" 
              @click="requestPasswordChange"
              >
              {{ !passwordChange ? 'Solicitar Cambio de Contraseña' : 'Cancelar Cambio de Contraseña' }}
            </v-btn>
          </v-card-actions>

          <v-card-actions>
            <v-btn color="orange-accent-4" @click="showPauseDialog">Pausar Cuenta</v-btn>
          </v-card-actions>
          
          <v-card-actions>
            <v-btn color="error" @click="showDeleteDialog">Cerrar Cuenta</v-btn>
          </v-card-actions>

        </div>


    </form>
  </div>

  <v-dialog v-model="dialog" persistent max-width="290">
    <v-card>
      <v-card-title class="headline">Pausar Cuenta</v-card-title>
      <v-card-text>¿Estás seguro de que quieres pausar tu cuenta?</v-card-text>
      <v-card-text>Podrás reactivarla ingresando en tu cuenta de nuevo.</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="dialog = false">Cancelar</v-btn>
        <v-btn color="green darken-1" text @click="pauseAccount">Aceptar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="dialogDeleteAccount" persistent max-width="290">
    <v-card>
      <v-card-title class="headline">Borrar Cuenta</v-card-title>
      <v-card-text>¿Estás seguro de que quieres borrar tu cuenta?</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="dialogDeleteAccount = false">Cancelar</v-btn>
        <v-btn color="green darken-1" text @click="deleteAccount">Aceptar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  </template>
  
  <script>
import axios from 'axios';
import auth from "@/services/auth.js";


  export default {
    data: () => ({
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        new_password: "",
        new_password_repeat: "",
        show1: false,
        show2: false,
        show3: false,
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
        },
        passwordChange: false,
        user: {
          username: "",
          first_name: "",
          last_name: "",
          email: "",
        },
        urlUser: 'http://localhost:8000/api/v1/users/',
        errorMessage: "",
        updatedMessage: "",
        dialog: false,
        dialogDeleteAccount: false,
    }),
    async created() {
      this.fetchUser();
      this.resetMessages();
      console.log('Obtener datos del perfil');
    },
    methods: {
      fetchUser() {
        console.log('Obtener datos del usuario: FETCH USER');
        const userId = localStorage.getItem('user_id');
        try{
          axios.get(`${this.urlUser}${userId}/detail/`)
            .then(response => {
              this.user = response.data;
              console.log('Datos del usuario', this.user);
              this.username = this.user.username;
              this.first_name = this.user.first_name;
              this.last_name = this.user.last_name;
              this.email = this.user.email;
              console.log('Datos del usuario obtenidos');

            });
        } catch (error) {
          console.log('Error al obtener datos del usuario', error);
        }
      },

      updateProfile() {
        if (this.passwordChange) {
          this.changePassword();
        } else {
          console.log('Actualizar perfil', this.username);
          const updateUser = {
            username: this.username,
            first_name: this.first_name,
            last_name: this.last_name,
            email: this.email,
          };
          console.log('Datos del usuario a actualizar', updateUser);
          try{
            const userId = localStorage.getItem('user_id');
            console.log('ID del usuario a actualizar', userId);
            axios.put(`${this.urlUser}${userId}/update/`, updateUser)
              .then(response => {
                console.log('Perfil actualizado');
                this.updatedMessage = 'Perfil actualizado correctamente';
                this.fetchUser();
              })
              .catch(error => {
                console.log('Error al actualizar perfil 1', error);
                this.errorMessage = 'Algo salió mal al actualizar el perfil';
              });
          } catch (error) {
            console.log('Error al actualizar perfil 2', error);
            this.errorMessage = 'Algo salió mal al actualizar el perfil';
          }
        }
      },
      requestPasswordChange() {
        this.passwordChange = !this.passwordChange;
        this.resetMessages();
      },
      changePassword() {
        console.log('Cambiar contraseña');
        if (this.new_password !== this.new_password_repeat) {
          console.log('Las contraseñas no coinciden');
          this.errorMessage = "Las contraseñas no coinciden";
          return;
        }
        const changePassword = {
          old_password: this.password,
          new_password: this.new_password,
        };
        try{
          const userId = localStorage.getItem('user_id');
          const token = localStorage.getItem('accessToken');
          axios.put(`${this.urlUser}${userId}/change_password/`, changePassword,
          {headers: { Authorization: `Bearer ${token}`} 
          })
            .then(response => {
              console.log('Contraseña cambiada');
              this.passwordChange = false;
              this.password = "";
              this.new_password = "";
              this.new_password_repeat = "";
              console.log('Mensaje de cambio de contraseña', response.data.message);
              this.updatedMessage = response.data.message;
            })
            .catch(error => {
              console.log('Error al cambiar contraseña 1', error);
              if(error.response && error.response.data){
                if (error.response.data.new_password && error.response.data.new_password[0] !== undefined)
                {
                  this.errorMessage = 'Algo salió mal con la contraseña nueva';
                  console.log('Error en mensaje de contraseña new_password',this.errorMessage);
                } else if (error.response.data.old_password && error.response.data.old_password[0] !== undefined) {
                  this.errorMessage = 'Algo salió mal con la contraseña actual';
                  console.log('Error en mensaje de contraseña old_password',this.errorMessage);
                } else {
                  this.errorMessage = 'Algo salió mal con el cambio de contraseña';
                }
            }
            })

        } catch (error) {
          console.log('Error al cambiar contraseña 2', error);
          if (error.response.data.new_password[0] !== undefined)
            {
              this.errorMessage = error.response.data.new_password[0];
            } else if (error.response.data.old_password[0] !== undefined){
              this.errorMessage = error.response.data.old_password[0];
            } else {
              this.errorMessage = 'Algo salió mal con el cambio de contraseña';
            }
        }
      },
      resetMessages() {
        this.errorMessage = "";
        this.updatedMessage = "";
      },
      pauseAccount() {
        console.log('Pausar cuenta');
        this.dialog = true;
        const userId = localStorage.getItem('user_id');
        const token = localStorage.getItem('accessToken');
 
        const data = {
          username: this.username,
          is_active: false,
        };
        try{
          axios.put(`${this.urlUser}${userId}/update/`,data,
          {headers: { Authorization: `Bearer ${token}`} 
          })
            .then(response => {
              console.log('Cuenta pausada');
              this.updatedMessage = 'Cuenta pausada correctamente';
              console.log('Llamando a auth.logout()')
              auth.logout();
              console.log('Redirigiendo a login');
              this.$router.push("/login");
            })
            .catch(error => {
              console.log('Error al pausar cuenta 1', error);
              this.errorMessage = 'Algo salió mal al pausar la cuenta';
            });
        } catch (error) {
          console.log('Error al pausar cuenta 2', error);
          this.errorMessage = 'Algo salió mal al pausar la cuenta';
        }
      },
      showPauseDialog() {
        console.log('Mostrar diálogo de pausar cuenta');
        this.dialog = true;
      },
      showDeleteDialog(){
        console.log('Mostrar diálogo de cerrar cuenta');
        this.dialogDeleteAccount = true;
      },
      
      deleteAccount() {
        console.log('Cerrar cuenta');
        const user_id = localStorage.getItem('user_id');
        try{
          axios.delete(`${this.urlUser}${user_id}/delete/`)
            .then(response => {
              console.log('Cuenta cerrada:', response);
              this.$router.push("/login");
              auth.logout();
            })
            .catch(error => {
              console.error('Error al cerrar cuenta:', error);
            });
        } catch{
          console.log('Error al cerrar cuenta');
        }

      },
    },
  };
  </script>
  <style lang="sass" src="@/assets/sass/pages/profile/_profile.sass" scoped></style>