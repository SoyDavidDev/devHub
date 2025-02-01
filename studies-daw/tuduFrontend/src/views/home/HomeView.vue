<template>
  <ShareButton :tasks="sharedTodoList" :isHomeView = "true"/>
</template>

<script>
import { defineComponent, ref } from "vue";

// Components
import ShareButton from "@/components/sharing/ShareButton.vue";

export default defineComponent({
  name: "HomeView",

  components: {
    ShareButton,
  },
  setup() {
    const sharedTodoList = ref([]);

    return {
      sharedTodoList,
    };
  },
});
</script>
