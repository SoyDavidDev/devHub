<template>
  <div class="login">
    <h1 class="title">Log in</h1>
    <form action id="main-form" class="form" @submit.prevent="handleSubmit">

      <div class="form-email" v-if="resetPassword">
        <label class="form-label" for="#email">Email:</label>
          <v-text-field
            v-model="email"
            class="form-input email-input"
            type="email"
            id="email"
            required
            placeholder="Email"
          />
      </div>

      <div class="form-container" v-if="!resetPassword">
        <label class="form-label" for="#username"
        >Username:</label>
        <v-text-field
          v-model="username"
          type="text"
          id="username"
          required
          placeholder="Username"
          filled
          color="transparent"
          v-show="!resetPassword"
        />
        <label class="form-label" for="#password"
        >Password:</label>
          <v-text-field
            v-model="password"
            :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            hint="At least 8 characters"
            counter
            filled
            color="transparent"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show = !show"
            v-show="!resetPassword"
          />
        <p v-show="error" class="error">
          Has introducido mal tu usuario y/o contraseña.
        </p>
        <p v-show="message" class="message">
          {{message}}
        </p>

      </div>

      <!-- revisar función de botones submit y hacer iuno para login y otro
      para resetpassword -->
      <div class="form-actions">
        <input class="form-submit" type="submit" :value="resetPassword ? 'Recordar contraseña' : 'Iniciar sesión'" />      
        <v-card-actions>
          <v-btn color="secondary" @click="resetPasswordChange">{{!resetPassword ? 'Recordar Contraseña' : 'Iniciar Sesión'}}</v-btn>
        </v-card-actions>
      </div>
    </form>
  </div>


  <v-dialog v-model="dialog" persistent max-width="500">
        <v-card class="d-flex flex-column align-center justify-center">
        <v-card-title class="headline">
            Email enviado
        </v-card-title>
            <v-card-subtitle>
            Por favor, revisa tu correo para cambiar tu contraseña
            </v-card-subtitle>
            <v-card-actions class="justify-center">
            <v-btn icon color="green darken-1" @click="closeDialog">
                Cerrar
                <v-icon>mdi-close</v-icon>
            </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import auth from "@/services/auth.js";

export default {
  data: () => ({
    username: "",
    password: "",
    error: false,
    show: false,
    resetPassword: false,
    rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => ('The email and password you entered don\'t match')
        },
    message: "",
    user_id: "",
    wasInactive: false,
    email: "",
    dialog: false,
  }),
  methods: {

    handleSubmit(){
      if (this.resetPassword){
        this.resetPasswordChange();
        this.dialog = true;
      } else {
        this.login();
      }
    },
    async login() {
      console.log("Login");
      console.log(this.username);
      console.log(this.password);
      try{
        const response = await auth.login(this.username, this.password);
        if (response.access){
          localStorage.setItem("accessToken", response.access);
          localStorage.setItem('userId', response.user_id);
          localStorage.setItem('was_inactive', String(response.was_inactive));
          this.wasInactive = response.was_inactive;
          console.log('Was inactive after login: ', this.wasInactive);
          console.log('Response: ',response);
          this.$store.commit("setLoggedIn", true);
          console.log('Logged in');
          this.$router.push('/mylists');
          

        } else{
          this.error = true;
          this.$store.commit("setLoggedIn", false);
        }   
      } catch (error) {
        console.log("Error con la response");
        this.error = true;
        console.log(error);
        this.$store.commit("setLoggedIn", false);

      }
    },
    async resetPasswordChange() {
      this.resetPassword = !this.resetPassword;
      console.log('Solicitar cambio de contraseña');
      if (this.resetPassword){
        try{
          const response = await auth.resetPassword(this.email);
          console.log(response);
        } catch (error){
          console.log("Error con la response");
          this.error = true;
          console.log(error);
        }
      }
    },
    closeDialog(){
      this.dialog = false;
    }

  },
};
</script>
<style lang="sass" src="@/assets/sass/pages/login/_login.sass" scoped></style>