<template>
    <div class="image">
    <img
        :class="Sass"
        decoding="async"
        :loading="attrs.notLazy ? 'eager' : 'lazy'"
        :src="src"
        :alt="alt"
        :width="parseInt(width)"
        :height="parseInt(height)"
        :style="{ maxWidth: '100%', height: 'auto', objectFit: 'cover' }"
    >
    <source
        v-for="(source, index) in sources"
        :key="index"
        :srcset="source.srcset"
        :media="source.media"
        :type="source.type"
    >
    </div>
</template>

<script>
export default {
    name: 'BasicImage',
    props: {
        // fit icons on apple device
        isIcon: {
            type: Boolean,
            required: false, 
            default: false
        },
        // SRC from image like url or path
        src: {
            type: String,
            required: false
        },
        // Alt attribute to image, refers the content of picture
        alt: {
            type: String,
            required: false
        },
        // Default width space to preserve image size
        width: {
            type: Number, 
            default: 100,
        },
        // Default height space to preserve image size
        height: {
            type: Number,
            default: 100,
       },
        // List of src and media sizes depending on the screen size
        sources: {
            type: Array,
            required: false
        },
        // Attributes to performance or filters to image
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                needContrast: false,
                notLazy: true 
            })
        },
        // Type and shape of border radius on image: full (all sides) / top (only top sides) / circle ( circular sides )
        type: {
            type: String,
            required: false, 
            default: "full"
        },
        // Value of border radius: none / xs / s / m / l / xl
        radius:{  // (none,0px) (xs,5px) (s,10px) (m,20px) (l,25px) (xl,40px)
            type: String,
            required: false,
            default: "none"
        }
    },
    computed: {
        Sass() {
            if(this.isIcon) return ''
            return `image-${this.type}-${this.radius}-${this.attrs.needContrast == true ? 'contrast' : 'noContrast'}`

        },
    }
};
</script>

<style lang="sass" src="@/assets/sass/pages/about/_how-we-work.sass" scoped>
</style>