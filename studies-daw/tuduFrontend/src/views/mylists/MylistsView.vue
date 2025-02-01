<template>
    <v-container>
        <v-row>
        <v-col cols="12">
            <h1 class="title">Mis listas</h1>
        </v-col>
        </v-row>

        <v-row>
        <v-col cols="12">
            <v-btn
                class="create" 
                color="primary" 
                text to="/list/create"
                >
                Crear lista
            </v-btn>
        </v-col>
        </v-row>
        
        <v-row>
            <v-col
            v-for="list of lists" 
            :key="list.id"
            cols="12"
            sm="6"
            md="4"
            lg="3"
            >
                <v-card
                    class="mx-auto"
                    max-width="344"
                    hover
                >
                    <v-card-item @click.stop="goToList(list.user_id, list.id)">
                        <v-card-title>
                            {{ list.title }}
                        </v-card-title>
                    </v-card-item>
                    <div class="buttons">
                        <v-btn
                        class="edit"
                        append-icon="mdi-account-circle"
                        text
                        @click.stop="goToEditList(list.user_id, list.id)"
                        >
                        <template v-slot:append>
                            <v-icon>mdi-pencil</v-icon>
                        </template>
                        Editar
                        </v-btn>

                        <v-btn
                        class="delete"
                        text
                        @click.stop="deleteList(list.id)"
                        >
                        <template v-slot:append>
                            <v-icon>mdi-delete</v-icon>
                        </template>
                        Eliminar
                        </v-btn>
                    </div>
                </v-card>

            </v-col>
        </v-row>
    </v-container>

    <v-dialog v-model="dialog" persistent max-width="290">
        <v-card class="d-flex flex-column align-center justify-center">
        <v-card-title class="headline">
            Bienvenido de nuevo!
        </v-card-title>
            <v-card-subtitle>
            Vuelve a disfrutar de tus listas Tudú!
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
import axios from 'axios';

export default {
    data() {
        return {
            lists: [],
            urlLists: "http://127.0.0.1:8000/api/v1/lists/",
            dialog: false,
            wasInactive: false,
        }
    },
    created() {
        this.wasInactive = localStorage.getItem('was_inactive') === 'true';
        this.dialog = this.wasInactive;
        this.fetchLists();
    },
    methods: {
        fetchLists() {
            const userId = localStorage.getItem('user_id');
            console.log('User ID:',userId);
            axios.get(`http://127.0.0.1:8000/api/v1/users/${userId}/lists/`)
                .then(response => {
                    this.lists = response.data;
                    console.log('Las listas',this.lists);
                })
                .catch(error => {
                    console.error('Error fetching lists:', error);
                });
        },

        goToEditList(userId, listId) {
        setTimeout(() => {
            this.$router.push(`/list/edit/${userId}/${listId}`);
        }, 0);
        },
        goToList(userId, listId) {
            this.$router.push(`/list/${userId}/${listId}`);
        },
        deleteList(listId){
            axios.delete(this.urlLists + listId + '/delete/')
            .then(response => {
                console.log('List deleted:', response);
                this.fetchLists();
            })
            .catch(error => {
                console.error('Error deleting list:', error);
            });
        },
        closeDialog() {
            this.dialog = false;
            this.wasInactive = false;
            localStorage.setItem('was_inactive', 'false');
            console.log('Was inactive after close dialog: ', this.wasInactive);
        },

    }
}
</script>
<style lang="sass" src="@/assets/sass/pages/mylists/_mylists.sass" ></style>