<script setup>
import { resolveImage } from "@/assets/local-images.js";

const props = defineProps({
    folder: {
        type: String,
        required: true
    },
    imgSrc: {
        type: String,
        required: true
    },
    imgAlt: {
        type: String,
        default: ""
    },
    description: {
        type: String,
        default: null
    },
    isSmallImg: {
        type: Boolean,
        default: false
    }
});

const linkPrefix = "https://static.clashpost.com/upgrade/" + props.folder + "/";
const imgLinkOriginal = resolveImage(linkPrefix + props.imgSrc);
</script>

<template>
    <div class="cp-unit-info">
        <picture :class="props.isSmallImg ? 'cp-unit-info-media cp-unit-info-media-sm' : 'cp-unit-info-media'">
            <img :src="imgLinkOriginal" :alt="props.imgAlt" />
        </picture>
        <p v-if="props.description" v-html="props.description"></p>
    </div>
</template>

<style lang="scss">
@use '@/assets/mixins.scss' as *;

.cp-unit-info {
    text-align: center;
    margin: 0.75rem 0;

    p {
        font-weight: 700;
    }
}

.cp-unit-info-media {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 240px;

    img {
        width: auto;
        height: auto;
    }
}

.cp-unit-info-media-sm {
    height: 160px;
}

@media (min-width: $cp-col-tablat) {
    .cp-unit-info-media {
        height: 300px;
    }
    
    .cp-unit-info-media-sm {
        height: 200px;
    }
}
</style>
