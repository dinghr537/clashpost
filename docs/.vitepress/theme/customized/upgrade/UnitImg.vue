<script setup>
import { onMounted, ref } from "vue";
import { resolveImage, imagePlaceholder } from "@/assets/local-images.js";

const props = defineProps({
    imgTitle: {
        type: String,
        required: true
    },
    imgSrc: {
        type: String,
        required: true
    },
    imgHd: {
        type: String,
        default: null
    }
});

const imgItemRef = ref();
const imgSrcOriginal = props.imgSrc;

onMounted(() => {
    // 确定图片链接
    const refDom = imgItemRef.value;
    const folder = refDom.parentNode.getAttribute("data-folder");
    const linkPrefix = "https://static.clashpost.com/upgrade/" + folder + "/";
    
    const image = refDom.querySelector("img");
    image.setAttribute("src", resolveImage(linkPrefix + imgSrcOriginal));
    const hdImage = props.imgHd ? resolveImage(linkPrefix + props.imgHd) : imagePlaceholder;
    if (hdImage !== imagePlaceholder) image.setAttribute("data-src-hd", hdImage);

});
</script>

<template>
    <div class="cp-unit-img-item" ref="imgItemRef">
        <div class="cp-unit-img-title">{{ props.imgTitle }}</div>
        <picture>
            <img loading="lazy" class="cp-unit-img" :src="imagePlaceholder" alt="" />
        </picture>
    </div>
</template>

<style lang="scss">
@use '@/assets/mixins.scss' as *;

.cp-unit-img-item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 5rem;
    min-height: 6rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}

@media (min-width: $cp-col-tablat) {
    .cp-unit-img-item {
        margin-right: 0.75rem;
        margin-bottom: 0.75rem;
    }
}

.cp-unit-img-title {
    margin-bottom: 0.125rem;
}

.cp-unit-img {
    width: auto;
    height: auto;
    max-width: 5rem;
    max-height: 6rem;
}
</style>