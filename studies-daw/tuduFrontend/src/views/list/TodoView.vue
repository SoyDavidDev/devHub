<template>
  <h1></h1>
<ShareButton :tasks="localTasks" @new-todo='handleNewTask' :isHomeView = "false"/>
<TodoComponent 
  :id="id" 
  :user_id="user_id" 
  :tasks="tasks" 
  @update-tasks="handleNewTask"
  />
</template>

<script>
import TodoComponent from "@/components/todos/TodoComponent.vue";
import ShareButton from "@/components/sharing/ShareButton.vue";
import axios from "axios";

export default {
  name: "TodoView",
  data() {
    return {
      id : this.$route.params.id,
      user_id : localStorage.getItem('user_id'),
      tasks: [],
      localTasks: [],
      urlListsTodos : 'http://localhost:8000/api/v1/lists/',
    
    };
  },
  components: {
    TodoComponent,
    ShareButton,
  },
  methods: {
    handleNewTask(newTasks){
      console.log('NUEVAS TAREAS Todoview', newTasks);
      this.tasks = newTasks;
    },

    async getTodos(){
      try{
        const response = await axios.get(this.urlListsTodos + this.id + '/');
        this.tasks = response.data;
        this.localTasks = response.data;
        console.log('TAREAS Todoview', this.tasks);
        console.log('TAREAS Todoview Localtasks', this.localTasks);
      } catch (error) {
        console.error(error);
        console.log('Error al obtener datos de tareas');
      }
    }
  },
  async created() {
    console.log('Información CREATED de Todoview');
    console.log('ID:', this.id);
    console.log('USER ID:', this.user_id);
    console.log('TASKS:', this.tasks);
    console.log('LOCAL TASKS:', this.localTasks);
    console.log('FIN Información CREATED de Todoview');
    try{
        const response = await axios.get(this.urlListsTodos + this.id + '/');
        this.tasks = response.data;
        this.localTasks = response.data;
        console.log('TAREAS Todoview', this.tasks);
        console.log('TAREAS Todoview Localtasks', this.localTasks);
      } catch (error) {
        console.error(error);
        console.log('Error al obtener datos de tareas');
      }
  },
} 


</script>