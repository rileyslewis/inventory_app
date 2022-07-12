export const Card = () => import('../../components/Card.vue' /* webpackChunkName: "components/card" */).then(c => wrapFunctional(c.default || c))
export const Form = () => import('../../components/Form.vue' /* webpackChunkName: "components/form" */).then(c => wrapFunctional(c.default || c))
export const Sidebar = () => import('../../components/Sidebar.vue' /* webpackChunkName: "components/sidebar" */).then(c => wrapFunctional(c.default || c))
export const Table = () => import('../../components/Table.vue' /* webpackChunkName: "components/table" */).then(c => wrapFunctional(c.default || c))

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
