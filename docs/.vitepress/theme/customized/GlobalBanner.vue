<script setup>
import { computed } from "vue";
import Callout from "@/components/Callout.vue";

const props = defineProps({ link: { type: String, default: "" } });
const isUpgrade = computed(() => props.link === "/upgrade" || props.link.startsWith("/upgrade/"));
</script>

<template>
    <Callout type="info" class="cp-callout-global-mark" v-if="isUpgrade">
        当前沿用原项目历史数据，各单位更新时间不同，尚未完成最新版本同步。已更新的内容会注明来源和同步日期。
    </Callout>
</template>

<style>
.cp-callout-global-mark { margin: 1rem 0 -0.5rem 0; }
</style>
