export default {
    publicRuntimeConfig: {
        baseURL: process.env.BASE_URL || 'http://0.0.0.0:5000/'
        
      },
    server: {
        port: 8080
    },
    buildModules: [
        "@nuxtjs/vuetify",
    ],
    modules: [
        "@nuxtjs/axios",
        "bootstrap-vue/nuxt",
        
    ],
    bootstrapVue: {
        bootstrapCSS: false,
        bootstrapVueCSS: false
    },
    components: true,
    
}