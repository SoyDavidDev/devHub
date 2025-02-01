<template>
    <div class="register">
      <h1 class="title">Sign Up</h1>
      <form action class="form" @submit.prevent="register">

        <div class="form-container">
          <label class="form-label" for="#nane">Username:</label>
          <v-text-field
            v-model="username"
            class="form-input"
            type="text"
            id="username"
            required
            placeholder="Username"
          />
          <label class="form-label" for="#first_name">First Name:</label>
          <v-text-field
            v-model="first_name"
            class="form-input"
            type="text"
            id="first_name"
            required
            placeholder="First Name"
          />
          <label class="form-label" for="#last_name">Last Name:</label>
          <v-text-field
            v-model="last_name"
            class="form-input"
            type="text"
            id="last_name"
            required
            placeholder="Last Name"
          />
          <label class="form-label" for="#email">Email:</label>
          <v-text-field
            v-model="email"
            class="form-input"
            type="email"
            id="email"
            required
            placeholder="Email"
          />
          <label class="form-label" for="#password">Password:</label>
          <v-text-field
            v-model="password"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            hint="At least 8 characters"
            counter
            @click:append="show = !show"
            class="form-input"
            id="password"
          />
          <label class="form-label" for="#password-repeat"
          >Repeat your password:</label
          >
          <v-text-field
            v-model="passwordRepeat"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            hint="At least 8 characters"
            counter
            @click:append="show = !show"
            class="form-input"
            id="password-repeat"
          />

        </div>

        <div class="form-actions">
          <p class="error">
            {{errorMessage}}
          </p>
  
          <input class="form-submit" type="submit" value="Sign Up" />
          <v-card-actions>
            <v-btn color="secondary" :to="'/login'">Iniciar sesión</v-btn>      
          </v-card-actions>

        </div>
      </form>
    </div>
  </template>
  
  <script>
  import auth from "@/services/auth.js"

  export default {
    data: () => ({
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        passwordRepeat: "",
        show: false,
        errorMessage: "",
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
        }
    }),
    methods: {
      async register() {
        try{
          const response = await auth.register(
            this.username,
            this.first_name, 
            this.last_name,
            this.email, 
            this.password);
          
          this.$router.push('/login');
        }catch(e){
          console.log("ERROR EN LA CONEXIÓN",e);
          if (e.response && e.response.status === 400) {
            console.log('User already exists')
            this.errorMessage = e.response.data.username[0];
            console.log('Error en register view ',this.errorMessage);
          } else{
            console.log('An error occurred', e)
          }
        }
      },
    },
  };
  </script>
  
  <style lang="sass" src="@/assets/sass/pages/register/_register.sass" scoped></style>
