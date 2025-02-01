<template>
    <div class="about">
      <h1> {{ textAbout.title.text_h1 }}</h1>
        <p>{{ textAbout.title.text }}</p>
    </div> 
    <section class="about__header">
    <BasicImage
        :src="textAbout.header.image.src"
        :alt="textAbout.header.image.alt"
        :width="textAbout.header.image.width"
        :height="textAbout.header.image.height"
        :sources="textAbout.header.image.sources"
        :attrs="textAbout.header.image.attrs"
        :type="textAbout.header.image.type"
        :radius="textAbout.header.image.radius"
        class="about__one__image"
    />
    </section>

    <section class="about__one">
        <div class="about__one__text">
            <img :src="textAbout.one.icon" alt="About one" class="about__one__image">
            <h2>{{ textAbout.one.title }}</h2>
            <p>{{ textAbout.one.paragrah.text_one }}</p>
            <p>{{ textAbout.one.paragrah.text_two }}</p>
            <p>{{ textAbout.one.paragrah.text_three }}</p>
            <p>{{ textAbout.one.paragrah.text_four }}</p>
        </div>
        <BasicImage
            :src="textAbout.one.image.src"
            :alt="textAbout.one.image.alt"
            :width="textAbout.one.image.width"
            :height="textAbout.one.image.height"
            :sources="textAbout.one.image.sources"
            :attrs="textAbout.one.image.attrs"
            :type="textAbout.one.image.type"
            :radius="textAbout.one.image.radius"
            class="about__one__image"
        />
    </section>
    <section class="about__four">
        <div>
            <img :src="textAbout.four.icon" alt="About four" class="about__four__icon">
            <h2>{{ textAbout.four.title }}</h2>
            <p>{{ textAbout.four.paragrah.text_one }}</p>
            <p>{{ textAbout.four.paragrah.text_two }}</p>
            <p>{{ textAbout.four.paragrah.text_three }}</p>
            <p>{{ textAbout.four.paragrah.text_four }}</p>
        </div>
        <BasicImage
            :src="textAbout.four.image.src"
            :alt="textAbout.four.image.alt"
            :width="textAbout.four.image.width"
            :height="textAbout.four.image.height"
            :sources="textAbout.four.image.sources"
            :attrs="textAbout.four.image.attrs"
            :type="textAbout.four.image.type"
            :radius="textAbout.four.image.radius"
            class="about__four__image"
        />
    </section>

    <section class="about__five">
        <div>
            <img :src="textAbout.five.icon" alt="About five" class="about__five__icon">
            <h2>{{ textAbout.five.title }}</h2>
            <p>{{ textAbout.five.paragrah.text_one }}</p>
            <p>{{ textAbout.five.paragrah.text_two }}</p>
            <p>{{ textAbout.five.paragrah.text_three }}</p>
            <p>{{ textAbout.five.paragrah.text_four }}</p>
        </div>
        <BasicImage
            :src="textAbout.five.image.src"
            :alt="textAbout.five.image.alt"
            :width="textAbout.five.image.width"
            :height="textAbout.five.image.height"
            :sources="textAbout.five.image.sources"
            :attrs="textAbout.five.image.attrs"
            :type="textAbout.five.image.type"
            :radius="textAbout.five.image.radius"
            class="about__five__image"
        />
    </section>

    <section class="about__six">
        <div>
            <img :src="textAbout.six.icon" alt="About six" class="about__six__icon">
            <h2>{{ textAbout.six.title }}</h2>
            <p>{{ textAbout.six.paragrah.text_one }}</p>
            <p>{{ textAbout.six.paragrah.text_two }}</p>
            <p>{{ textAbout.six.paragrah.text_three }}</p>
            <p>{{ textAbout.six.paragrah.text_four }}</p>
            <p>{{ textAbout.six.paragrah.text_five }}</p>
        </div>
        <BasicImage
            :src="textAbout.six.image.src"
            :alt="textAbout.six.image.alt"
            :width="textAbout.six.image.width"
            :height="textAbout.six.image.height"
            :sources="textAbout.six.image.sources"
            :attrs="textAbout.six.image.attrs"
            :type="textAbout.six.image.type"
            :radius="textAbout.six.image.radius"
            class="about__six__image"
        />
    </section>

    <section class="about__seven">
        <div>
            <img :src="textAbout.seven.icon" alt="About seven" class="about__seven__icon">
            <h2>{{ textAbout.seven.title }}</h2>
            <p>{{ textAbout.seven.paragrah.text_one }}</p>
            <p>{{ textAbout.seven.paragrah.text_two }}</p>
            <p>{{ textAbout.seven.paragrah.text_three }}</p>
            <p>{{ textAbout.seven.paragrah.text_four }}</p>
            <p>{{ textAbout.seven.paragrah.text_five }}</p>
        </div>
        <BasicImage
            :src="textAbout.seven.image.src"
            :alt="textAbout.seven.image.alt"
            :width="textAbout.seven.image.width"
            :height="textAbout.seven.image.height"
            :sources="textAbout.seven.image.sources"
            :attrs="textAbout.seven.image.attrs"
            :type="textAbout.seven.image.type"
            :radius="textAbout.seven.image.radius"
            class="about__seven__image"
        />
    </section>
</template>

<script>
import BasicImage from '@/components/basic/image/index.vue'

export default {
    name: 'AboutView',
    components: { 
        BasicImage 
    },
    data() {
        return {
            textAbout: require('@/content/pages/about/text.js')
        }
    },
};
</script>

<style lang="sass" src="@/assets/sass/pages/about/_how-we-work.sass" scoped></style>