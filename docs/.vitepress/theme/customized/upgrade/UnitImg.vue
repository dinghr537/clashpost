<script setup>
import { nextTick, onMounted, ref } from "vue";
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
const previewRef = ref();
const imageSrc = ref(imagePlaceholder);
const previewSrc = ref(imagePlaceholder);
const previewOpen = ref(false);
const imgSrcOriginal = props.imgSrc;

onMounted(() => {
    const refDom = imgItemRef.value;
    const folder = refDom.parentNode.getAttribute("data-folder");
    const linkPrefix = "https://static.clashpost.com/upgrade/" + folder + "/";
    imageSrc.value = resolveImage(linkPrefix + imgSrcOriginal);

    const sourceHd = props.imgHd ? linkPrefix + props.imgHd : "";
    const localHd = sourceHd ? resolveImage(sourceHd) : imagePlaceholder;
    previewSrc.value = localHd !== imagePlaceholder ? localHd : imageSrc.value;
});

async function openPreview() {
    if (imageSrc.value === imagePlaceholder) return;
    previewOpen.value = true;
    await nextTick();
    previewRef.value?.showModal();
}

function closePreview() {
    previewRef.value?.close();
}
</script>

<template>
    <div class="cp-unit-img-item" ref="imgItemRef">
        <div class="cp-unit-img-title">{{ props.imgTitle }}</div>
        <button type="button" class="cp-unit-img-button" :aria-label="`查看${props.imgTitle}图片`" @click="openPreview">
            <img loading="lazy" class="cp-unit-img" :src="imageSrc" alt="" />
        </button>
        <dialog ref="previewRef" class="cp-unit-img-preview" :aria-label="`${props.imgTitle}图片`"
            @click.self="closePreview" @close="previewOpen = false">
            <div class="cp-unit-img-preview-content" v-if="previewOpen">
                <div class="cp-unit-img-preview-header">
                    <span>{{ props.imgTitle }}</span>
                    <button type="button" class="cp-unit-img-preview-close" aria-label="关闭图片" @click="closePreview">×</button>
                </div>
                <img :src="previewSrc" :alt="props.imgTitle" />
            </div>
        </dialog>
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

.cp-unit-img-button {
    padding: 0;
    border: 0;
    background: transparent;
    cursor: zoom-in;
}

.cp-unit-img-button:focus-visible,
.cp-unit-img-preview-close:focus-visible {
    outline: 2px solid currentColor;
    outline-offset: 3px;
}

.cp-unit-img-preview {
    max-width: min(94vw, 1200px);
    max-height: 94vh;
    padding: 1rem;
    border: 0;
    border-radius: 0.5rem;
    color: var(--cp-text-light);
    background: var(--cp-page-bg-light);
}

.cp-unit-img-preview::backdrop {
    background: rgba(0, 0, 0, 0.7);
}

.cp-unit-img-preview-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.cp-unit-img-preview-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    gap: 1rem;
}

.cp-unit-img-preview-close {
    padding: 0 0.25rem;
    border: 0;
    color: inherit;
    background: transparent;
    font-size: 1.75rem;
    line-height: 1;
    cursor: pointer;
}

.cp-unit-img-preview-content > img {
    max-width: min(86vw, 1120px);
    max-height: 75vh;
    width: auto;
    height: auto;
    object-fit: contain;
}

body.cp-theme-dark .cp-unit-img-preview {
    color: var(--cp-text-dark);
    background: var(--cp-page-bg-dark);
}
</style>
