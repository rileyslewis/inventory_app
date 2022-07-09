<template>
    <v-app>
        <v-main>
        <Sidebar />
       <!-- <v-app-bar color="purple" dense><v-card-text class="white--text"> 

        </v-card-text></v-app-bar> -->
        
            <v-spacer></v-spacer>
            <v-container justify="center" align="center" >
                <client-only>
                    <Nuxt />
                </client-only>
                
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {

};

</script>

<style>
html { overflow-y: auto }

</style>