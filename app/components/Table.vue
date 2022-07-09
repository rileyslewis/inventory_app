<template>
  <v-card>
    <v-card-title>
      Inventory
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        ></v-text-field>
    </v-card-title>
    <v-data-table
    :headers="headers"
    :items="items"
    item-key="name"
    :loading="!items.length"
    loading-text="Loading.. Please wait"
    :search="search"
  >
    <template v-slot:[`item.edit`]="{ item }">
        <v-btn color="primary" @click="editItem(item)"> Edit </v-btn>
    </template>
    <template v-slot:[`item.delete`]="{ item }">
        <v-btn color="red" @click="deleteItem(item.id)"> Delete </v-btn>
    </template>
  </v-data-table>
  </v-card>
</template>

<script>
export default {
    data () {
      return {
        search: '',
        headers: [
          
          { text: 'ID', value: 'id' },
          { text: 'Name', value: 'name' },
          { text: 'Quantity', value: 'quantity' },
          { text: 'Edit', value: 'edit' },
          { text: 'Delete', value: 'delete' },
        ],
      }
    },
    computed: {
        items(){
            return this.$store.state.items.data
        }
    },
    async fetch() {
        this.$store.commit('items/storeData', (await this.$axios.get(this.$config.baseURL)).data)
    },
    methods: {
        editItem(item){
            this.$store.commit("item/storeId", item.id);
            this.$store.commit("item/storeName", item.name);
            this.$store.commit("item/storeQuantity", item.quantity);
        }, 
        async deleteItem(id) {
            await this.$axios.delete(this.$config.baseURL + id);
            this.$store.commit('items/storeData', (await this.$axios.get(this.$config.baseURL)).data);
        },
    }
  }
</script>

<style lang="scss" scoped>

</style>