<template>
<div class="profile-view">
    <h1 class="title">Gestión de perfil</h1>
    <form action class="form" @submit.prevent="updateProfile">

        <div class="form-passwordChanging">
          <label for="new_password" class="form-label">Nueva Contraseña:</label>
          <v-text-field 
            label="Nueva Contraseña" 
            :type="show1 ? 'text' : 'password'" 
            id="new_password"
            v-model="new_password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show1 = !show1"
          />
          <label for="new_password_repeat" class="form-label">Repetir Nueva Contraseña:</label> 
          <v-text-field 
            label="Repetir Nueva Contraseña" 
            :type="show2 ? 'text' : 'password'" 
            id="new_password_repeat"
            v-model="new_password_repeat"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show2 = !show2"
          />
        </div>
             
        <div class="form-actions">

          <div class="form-actions-messages">
            <p class="updated" v-if="!errorMessage">
              {{updatedMessage}}
            </p>
          </div>

          <input 
            class="form-submit" 
            type="submit" 
            value="Cambiar Contraseña"
          >
        </div>


    </form>
  </div>



  <v-dialog v-model="dialogChangeAccount" persistent max-width="290">
        <v-card class="d-flex flex-column align-center justify-center">
        <v-card-title class="headline">
            Contraseña cambiada con éxito!
        </v-card-title>
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

export default{
    data: () => ({
        token: "",
        password: "",
        error: false,
        message: "",
        show1: false,
        show2: false,
        dialogChangeAccount: false,
        new_password: "",
        new_password_repeat: "",
    }),
    async created(){
        const uid = this.$route.params.uid;
        const token = this.$route.params.token;
        try {
            const response = await auth.resetPasswordConfirm(uid, token);
            this.token = token;
            console.log(response);
            console.log("Vista de cambio de contraseña creada");
        } catch (error){
            console.log("Error en la creación de la vista de cambio de contraseña");
            console.log(error);
        }
    },
    methods: {
        async confirmResetPassword(){
            console.log("Confirmar cambio de contraseña");
            try{
                const response = await auth.confirmResetPassword(this.token, this.password );
                this.message = response.message;
            }catch(error){
                console.log("Error con la response");
                this.error = true;
                console.log(error);
            }
        },
    }
}

</script>