const { defineConfig } = require("@vue/cli-service");
module.exports = {
  transpileDependencies: [],

  css: {
    loaderOptions:{
      sass:{
        additionalData: `@import "@/assets/sass/theme/light/_color.sass"`
      }
    }
  },

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    },
  },
};