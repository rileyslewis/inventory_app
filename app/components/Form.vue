<template>

    <div
  class="fixed-top d-flex align-items-center justify-content-center"
  style="bottom: 0; overflow-y: auto"
>

    <v-form style="max-width: 400px;">
    <v-text-field v-if="id" v-model="id" label="ID to Edit" class="mb-2" ></v-text-field>
    <v-text-field v-model="name" label="Name" class="mb-2"></v-text-field>
    <v-text-field v-model="quantity" label="Quantity" class="mb-2"></v-text-field>
    <v-btn color="success" @click="submitItem({id, name, quantity})">
        {{id ? 'Edit' : 'Submit'}}
    </v-btn>
  </v-form>
</div>



</template>

<script>

export default {
    computed:{
        id:{
            get(){
                return this.$store.state.item.id
            },
            set(value){
                this.$store.commit("item/storeId", value)
            }
        },
        name:{
            get(){
                return this.$store.state.item.name
            },
            set(value){
                this.$store.commit("item/storeName", value)
            }
        },
        quantity:{
            get(){
                return this.$store.state.item.quantity
            },
            set(value){
                this.$store.commit("item/storeQuantity", value)
            }
        }
    },
    methods:{
        async submitItem(item){
            if(item.id){
                await this.$axios.put(this.$config.baseURL + item.id, item)
            }else{
                await this.$axios.post(this.$config.baseURL, item);
            }
            
            this.resetForm({id:0, name:'', quantity:0});
            await this.$store.commit("items/storeData", (await this.$axios.get(this.$config.baseURL)).data);
        },
        resetForm(item) {
            this.$store.commit("item/storeId", item.id);
            this.$store.commit("item/storeName", item.name);
            this.$store.commit("item/storeQuantity", item.quantity);
        }
    }
}

</script>

<style lang="scss" scoped>

</style>