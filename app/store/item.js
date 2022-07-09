export const state = () => ({
    id: 0,
    name: "",
    quantity: 0
})

export const mutations = {
    storeId: (state, data) => {
        state.id = data
    },
    storeName: (state, data) => {
        state.name = data
    },
    storeQuantity: (state, data) => {
        state.quantity = data
    }
}