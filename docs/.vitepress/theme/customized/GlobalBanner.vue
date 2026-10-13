<script setup>
import { computed } from "vue";
import { useData } from "vitepress";
import Callout from "@/components/Callout.vue";

const props = defineProps({ link: { type: String, default: "" } });
const isUpgrade = computed(() => props.link === "/upgrade" || props.link.startsWith("/upgrade/"));
const { frontmatter } = useData();
const syncedDate = computed(() => String(frontmatter.value.dataSyncedOn || "").slice(0, 10));
const isCategory = computed(() => props.link === "/upgrade" || props.link.startsWith("/upgrade/category/"));
</script>

<template>
    <Callout type="info" class="cp-callout-global-mark" v-if="isUpgrade">
        <template v-if="syncedDate">本页已同步 {{ syncedDate }} 的来源表格。以下费用和时间为基础值，月卡减免另行计算。</template>
        <template v-else-if="isCategory">数据同步日期：2026-10-13。已更新常驻单位、精工防御和部分临时单位；往期临时单位的历史数据会单独标注。</template>
        <template v-else>本页保留原项目历史数据，尚未重新核对当前来源；不能视为最新版本数据。</template>
    </Callout>
</template>

<style>
.cp-callout-global-mark { margin: 1rem 0 -0.5rem 0; }
</style>
