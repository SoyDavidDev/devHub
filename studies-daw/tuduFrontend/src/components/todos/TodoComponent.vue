<template>
  <v-container class="container">
    <v-row>
      <v-col>
        <BasicImage
        :src="imageBrand.header.image.src"
        :alt="imageBrand.header.image.alt"
        :width="imageBrand.header.image.width"
        :height="imageBrand.header.image.height"
        :sources="imageBrand.header.image.sources"
        :attrs="imageBrand.header.image.attrs"
        :type="imageBrand.header.image.type"
        :radius="imageBrand.header.image.radius"
        class="container__image"
        />      
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-sheet>
          <v-form ref="form" @submit.prevent="addTodo">
            <v-text-field
              v-model="newTodo.title"
              class= "input"
              :counter="40"
              :rules="newTodo.titleRules"
              label="Enter your tudú!"
            ></v-text-field>
            <v-textarea
              v-model="newTodo.description"
              autocomplete="Description"
              label="Description"
              :counter="250"
            ></v-textarea>
            <v-checkbox
              v-model="newTodo.completed"
              label="Is Completed?"
            ></v-checkbox>
            <v-btn
              color="primary"
              type="submit"
              class="mb-5"
            >Add tudú</v-btn>
            <v-list class="todos">
              <v-list-item
                v-for="(todo, index) in sortedTodoList()"
                :key="index"
                @click="toggleCompleted(index)"
                @contextmenu.prevent="deleteItem(index)"
                :class="{ completed: todo.completed }"
              >
              <div class="d-flex justify-space-between w-100">
                <div class = "v-list-item-component">
                  <h6>{{ todo.title }}</h6>
                  <span class="text-caption">{{ todo.description }}</span>
                </div>
                <v-btn 
                icon @click.stop="editItem(index)"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </div>
              </v-list-item>
            </v-list>
          </v-form>
          <small>Left click to toggle completed,
            <br><strong>Right click to delete</strong>
          </small>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import BasicImage from '@/components/basic/image/index.vue'

export default {
  components: {
    BasicImage,
  },
  props: ["id", "user_id", "tasks"],
  data() {
    return {
    todos: [],
    name : "TodoComponent",
    newTodo: this.initializeNewTodo(),
    todoList: [],
    urlUser: "http://127.0.0.1:8000/api/v1/users/",
    urlList: "http://127.0.0.1:8000/api/v1/lists/",
    urlTodo: "http://127.0.0.1:8000/api/v1/todos/",
    urlTodoCreate: "http://127.0.0.1:8000/api/v1/todos/create/",
    editingId: null,
    imageBrand: require('@/content/basic/branding/text.js'),

  };
  },
  async created() {
    try{
      const currentList = await this.getListsUser(this.user_id);
      console.log('Información CREATED de TodoComponent');
      console.log('Id de User', currentList.user_id);
      console.log('Listas de usuario', currentList);
      this.todoList = currentList.todos;
      console.log('FIN Información CREATED de TodoComponent')
    } catch (error) {
      console.error(error);
      console.log('Error al obtener datos de usuario');
    }
  },
  methods: {
    async getListsUser(userId) {
      console.log('INICIO GETLISTSUSER', userId);
      try{
        const userResponse = await axios.get(this.urlUser + userId + "/lists/");
        const userLists = userResponse.data;
        console.log('userLists función', userLists);

        const matchingList = userLists.find((list) => list.id == this.id);
        console.log('Lista que coincide', matchingList);
        console.log('FIN GETLISTSUSER');
        return matchingList;
      } catch (error) {
        console.error(error);
        console.log('Error al obtener datos de usuario de get user lists data');
      }
    },
    
    initializeNewTodo() {
      return {
        title: "",
        description: "",
        titleRules: [
          (v) => !!v || "Title is required",
          (v) => (v && v.length <= 40) || "Title must be less than 40 characters",
        ],
        completed: false,
        user_id: this.user_id,
        list_id: this.id,
      };
    },
    async getTodos() {
      console.log('Id de lista', this.id);
      console.log('Id de usuario', this.user_id);
      axios
        .get(`${this.urlList}${this.id}`)
        .then((response) => {
          console.log('Response de getTodos', response);
          console.log('Data de getTodos', response.data);
          this.todoList = response.data;
          this.sortedTodoList();
          console.log('La lista de todo de este usuario',this.todoList);
          this.$emit('update-tasks', this.todoList);
        })
        .catch((error) => {
          console.error(error);
          console.log('Error al obtener todos');
        });
    },
    async mounted() {
    this.getTodos();
    },
    async addTodo() {
      if (this.newTodo.title) {
        var data = {
          title: this.newTodo.title,
          completed: this.newTodo.completed,
          user_id: this.newTodo.user_id,
          list_id: this.newTodo.list_id,
        };
        console.log('Data de addTodo', data);
        if (this.newTodo.description) {
          data.description = this.newTodo.description;
        }
        console.log('Data de addTodo con descripción', data);
        try{
          const response = await axios.post(this.urlTodoCreate, data);      
          this.newTodo.title = "";
          this.newTodo.description = "";
          this.newTodo.completed = false;
          this.$refs.form.reset();
          this.todoList.unshift(response.data);

          this.$emit('new-task', this.todoList);
          console.log('Tarea agregada', response.data);
        } catch (error) {
          console.error(error);
          console.log('Error al agregar todo');
        }
      }
    },
    toggleCompleted(index)  {
      console.log('INICIO TOGGLE COMPLETED');
      this.todoList[index].completed = !this.todoList[index].completed;
      const url = this.urlTodo + this.todoList[index].id + "/update/";
      var data = {
        completed: this.todoList[index].completed,
      };
      axios.patch(url, data).then(() => {
        this.$emit('new-task', this.todoList);
        this.getTodos();
      });
    },
    async deleteItem(index) {
      try{
        console.log('INICIO DELETE ITEM')
        console.log('Id de item', this.todoList[index].id);
        const url = this.urlTodo + this.todoList[index].id + "/delete/";
        console.log('URL de item', url);
        await axios.delete(url);
        console.log('Item eliminado');
        this.todoList.splice(index, 1);
        this.$emit('new-task', this.todoList);

      } catch{
        console.log('Error al eliminar item');
      }
    },
    editItem(index){
      this.newTodo = {...this.todoList[index]};
      this.editingId = this.todoList[index].id;
      this.$emit('new-task', this.todoList);

    },
    sortedTodoList() {
      return this.todoList.sort((a, b) => {
        return a.completed - b.completed;
      });
    },
  }
};
</script>
<style lang="sass" src="@/assets/sass/components/todos/_todoComponent.sass" scoped>
</style>
