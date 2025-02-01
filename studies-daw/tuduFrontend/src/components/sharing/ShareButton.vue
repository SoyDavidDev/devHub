<template>
<div>
    <div class="container__buttons">
        <v-btn icon @click='shareOnWhatsApp'>
            <v-icon>mdi-whatsapp</v-icon>
        </v-btn>
        <v-btn icon @click='shareOnEmail'>
            <v-icon>mdi-email</v-icon>
        </v-btn>
        <v-btn icon @click='copyToClipboard'>
            <v-icon>mdi-content-copy</v-icon>
        </v-btn>
    </div>
    
    <SharedTodoComponent @new-todo='handleNewTask' v-if="isHomeView"/>
</div>
</template>

<script>
import SharedTodoComponent from '@/components/todos/SharedTodoComponent.vue';

export default{
    components: {
        SharedTodoComponent,
    },
    props: ['tasks', 'isHomeView',],
    data(){
        return {
            localTasks: [],
        }
    },
    watch:{
        tasks(newTasks){
            console.log('TAREAS watch', newTasks);
            this.localTasks = newTasks;
        }
    },
    methods: {
        handleNewTask(taskList){
            console.log('NUEVAS TAREAS handler HOMEVIEW', taskList);
            this.localTasks = taskList;
        },
        generateTasksText(){
        console.log('TAREAS generatetext', this.localTasks);
        const tasksText = this.localTasks.map((task, index) => {
            const status = task.completed ? 'Completada' : 'Pendiente';
            const description = task.description ? ` - ${task.description}` : '';
            return `${index + 1}. ${task.title}${description} (${status})`;
        }).join('\n');
        return tasksText;
    },
        shareOnWhatsApp(){
            const text = encodeURIComponent(`*Mira mi lista de tareas:*\n${this.generateTasksText()}`);
            console.log(text);
            window.open(`https://wa.me/?text=${text}`, '_blank');
        },
        shareOnEmail(){
            const subject = encodeURIComponent('Mi lista de tareas');
            const body = encodeURIComponent(this.generateTasksText());
            console.log(subject, body);
            window.open(`mailto:?subject=${subject}&body=${body}`, '_blank');
        },
        copyToClipboard(){
            const tasksText = this.generateTasksText();
            console.log(tasksText);
            navigator.clipboard.writeText(tasksText).then(() => {
                alert('Copiado al portapapeles');
            }).catch(() => {
                alert('Error al copiar al portapapeles');
            });
        },


    }
}
</script>
<style lang="sass" src="@/assets/sass/components/sharing/_shareButtons.sass" scoped> </style>