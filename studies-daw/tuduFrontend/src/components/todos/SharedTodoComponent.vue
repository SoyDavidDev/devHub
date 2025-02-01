<template>
  <v-container class="container">
    <div>
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
    </div>

    <v-row>
      <v-col>
        <v-sheet>
          <v-form ref="form">

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
              class="mb-5 button"
              @click.prevent="addTodo"
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
import BasicImage from '@/components/basic/image/index.vue'

export default {
  components: {
    BasicImage,
  },
  data: () => ({
    newTodo: {
      title: "",
      description: "",
      titleRules: [
        (v) => !!v || "Title is required",
        (v) => (v && v.length <= 40) || "Title must be less than 40 characters",
      ],
      completed: false,
      user: 1,
      list: 1,
    },
    sharedTodoList: [],
    editingId: null,
    imageBrand: require('@/content/basic/branding/text.js')
  }),
  methods: {
    addTodo() {
      if (this.newTodo.title) {
        var data = {
          title: this.newTodo.title,
          completed: this.newTodo.completed,
          user: this.newTodo.user,
          list: this.newTodo.list,
        };
        if (this.newTodo.description) {
          data.description = this.newTodo.description;
        }
        console.log('sharedTodoList',this.sharedTodoList);
        this.sharedTodoList.unshift(data);
        this.$emit('new-todo', this.sharedTodoList);
        this.newTodo.title = "";
        this.newTodo.description = "";
        this.newTodo.completed = false;
        this.$refs.form.reset();
      }
    },
    toggleCompleted(index)  {
      this.sharedTodoList[index].completed = !this.sharedTodoList[index].completed;
    },
    deleteItem(index) {
      this.sharedTodoList.splice(index, 1);
    },
    editItem(index){
      this.newTodo = this.sharedTodoList[index];
      this.editingId = index;
    },
    saveEdit(){
      this.sharedTodoList[this.editingId] = this.newTodo;
      this.newTodo = {
        title: "",
        description: "",
        completed: false,
        user: 1,
        list: 1,
      };
      this.editingId = null;
    },
    sortedTodoList(){
      return this.sharedTodoList.sort((a, b) => a.completed - b.completed);
    
    }
  }
};
</script>
<style lang="sass" src="@/assets/sass/components/todos/_shareToDoComponent.sass" scoped>
</style>
