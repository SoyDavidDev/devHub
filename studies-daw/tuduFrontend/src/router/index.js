import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/home/HomeView.vue";
import AboutView from "../views/about/AboutView.vue";
import LoginView from "../views/login/LoginView.vue";
import RegisterView from "../views/login/RegisterView.vue";
import MylistsView from "../views/mylists/MylistsView.vue";
import ListCreateView from "../views/list/ListCreateView.vue";
import ListEditView from "../views/list/ListEditView.vue";
import TodoView from "../views/list/TodoView.vue";
import ProfileView from "@/views/profile/ProfileView.vue";
import ResetPasswordConfirmView from "@/views/resetPass/ResetPasswordConfirmView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  { path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/mylists",
    name: "mylists",
    component: MylistsView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/list/create",
    name: "list-create",
    component: ListCreateView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/list/edit/:user_id/:id",
    name: "ListEditView",
    component: ListEditView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/list/:user_id/:id",
    name: "TodoView",
    component: TodoView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/reset-password-confirm/:uid/:token",
    name: "reset-password-confirm",
    component: ResetPasswordConfirmView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
