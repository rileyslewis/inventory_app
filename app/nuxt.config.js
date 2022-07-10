export default {
    publicRuntimeConfig: {
        baseURL: process.env.BASE_URL || 'http://0.0.0.0:8080/'
      },
    ngrok: {
        
        addr: 3000
    },
    
    buildModules: [
        "@nuxtjs/vuetify",
        "@nuxtjs/dotenv",
        
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