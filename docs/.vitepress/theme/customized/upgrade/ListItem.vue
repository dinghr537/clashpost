<script setup>
import { onMounted, ref } from "vue";
import { resolveImage, imagePlaceholder } from "@/assets/local-images.js";

const props = defineProps({
    name: {
        type: String,
        required: true
    },
    imgSrc: {
        type: String,
        required: true
    },
    link: {
        type: String,
        required: true
    },
    lazyLoading: {
        type: Boolean,
        default: true
    }
});

const unitLinkRef = ref();
const link = "/upgrade/" + props.link;

// 图片相关
const imgSrcOriginal = props.imgSrc;
const loadingValue = props.lazyLoading ? "lazy" : "eager";

onMounted(() => {
    // 确定图片链接
    const refDom = unitLinkRef.value;
    const folder = refDom.parentNode.getAttribute("data-folder");
    const link = resolveImage("https://static.clashpost.com/upgrade/" + folder + "/" + imgSrcOriginal);
    refDom.querySelector("img").setAttribute("src", link);

});
</script>

<template>
    <a class="cp-unit-card" :href="link" ref="unitLinkRef">
        <picture class="cp-unit-media">
            <img :loading="loadingValue" :src="imagePlaceholder" alt="" />
        </picture>
        <div class="cp-unit-text">{{ name }}</div>
    </a>
</template>

<style lang="scss">
@use '@/assets/mixins.scss' as *;

.cp-unit-card {
    width: 4.25rem;
    min-height: 5.375rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 1rem 0.5rem;
    padding-bottom: 0.375rem;
    border-radius: 0.375rem;
    border: var(--cp-border-light);

    &:hover, &:focus {
        text-decoration: none;
    }

    &:hover {
        background-color: rgb(243, 244, 246);
        border: 0.1rem solid rgb(209, 213, 219);
    }

    &:focus {
        border: 0.1rem solid var(--cp-primary-light);
    }
}

.cp-theme-dark .cp-unit-card {
    border: var(--cp-border-dark);

    &:hover {
        background-color: rgb(38, 38, 38);
        border: 0.1rem solid rgb(64, 64, 64);
    }

    &:focus {
        border: 0.1rem solid var(--cp-primary-dark);
    }
}

.cp-unit-media {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    width: 100%;
    height: 4.5rem;
    padding: 0.375rem 0;
}

@media (min-width: 600px) {
    .cp-unit-card {
        width: 5.25rem;
        min-height: 6.25rem;
    }

    .cp-unit-media {
        height: 5.625rem;
    }
}

@media (min-width: $cp-col-tablat-big) {
    .cp-unit-card {
        margin: 1rem 0.75rem;
        width: 5.625rem;
        min-height: 7.5rem;
    }

    .cp-unit-media {
        height: 6.375rem;
    }
}

.cp-unit-text {
    margin: auto;
    text-align: center;
    line-height: 1.25;
}
</style>