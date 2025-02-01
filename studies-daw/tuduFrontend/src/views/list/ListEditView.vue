<template>
    <v-container>
        <v-row>
            <v-col cols="12" sm="6" md="4" lg="3">
                <v-card
                class="mx-auto my-8"
                elevation="16"
                max-width="344"
                >
                    <v-card-title>
                        <h1>Editar lista</h1>
                    </v-card-title>

                    <v-card-text>
                        <v-form @submit.prevent="editList">
                            <v-text-field
                                v-model="list.title"
                                label="Nombre de la lista"
                            ></v-text-field>
                            <v-btn
                                color="primary"
                                type="submit"
                            >Editar lista</v-btn>
                        </v-form>
                    </v-card-text>
                    
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            list: {
                title: '',
            },
            urlList: "http://127.0.0.1:8000/api/v1/lists/",
            id: this.$route.params.id,
            user_id: this.$route.params.user_id,
        }
    },
    async created() {
        try {
            const response = await axios.get(this.urlList + this.id + '/detail/');
            this.list = response.data;
            console.log('Response de created', response);
            console.log('List', this.list);
            console.log('ID', this.id);
            console.log('Title of the list', response.data.title)
            this.list.title = response.data.title;
        } catch (error) {
            console.error(error);
            console.log('Error al cargar la lista.');
        }
    },
    methods: {
        async editList(){
            try {
                const update = {
                    title: this.list.title,
                    user_id: this.user_id,
                }
                console.log('Update', update);
                console.log('URL list', this.urlList + this.id + '/update/')
                const response = 
                await axios
                .put(
                    this.urlList + this.id + '/update/', 
                    update
                );

                this.list = response.data;
                console.log('Response de editList', response);
                console.log('Lista editada', this.list);

                this.$router.push('/mylists');
            } catch (error) {
                console.log(error);
                console.log('Error al editar la lista');
            }
        }
    }

} 
</script>