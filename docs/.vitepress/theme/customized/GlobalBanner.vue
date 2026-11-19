<script setup>
import { computed } from "vue";
import { useData } from "vitepress";
import Callout from "@/components/Callout.vue";

const props = defineProps({ link: { type: String, default: "" } });
const { frontmatter } = useData();
// Data dates and sources are listed at the bottom of each unit page. The banner
// only warns on unit pages that still carry the original project's historical
// data and have not been re-checked against a current source.
const isLegacyUnit = computed(() =>
    props.link.startsWith("/upgrade/") && !props.link.startsWith("/upgrade/category/") &&
    !frontmatter.value.dataSyncedOn && !frontmatter.value.dataVersionUpdatedOn && !frontmatter.value.dataReviewedOn);
</script>

<template>
    <Callout type="info" class="cp-callout-global-mark" v-if="isLegacyUnit">
        本页保留原项目历史数据，尚未重新核对当前来源；不能视为最新版本数据。
    </Callout>
</template>

<style>
.cp-callout-global-mark { margin: 1rem 0 -0.5rem 0; }
</style>
