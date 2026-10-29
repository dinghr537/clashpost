<script setup>
import { computed } from "vue";
import { useData } from "vitepress";
import Callout from "@/components/Callout.vue";

const props = defineProps({ link: { type: String, default: "" } });
const isUpgrade = computed(() => props.link === "/upgrade" || props.link.startsWith("/upgrade/"));
const { frontmatter } = useData();
const syncedDate = computed(() => String(frontmatter.value.dataSyncedOn || "").slice(0, 10));
const reviewedDate = computed(() => String(frontmatter.value.dataReviewedOn || "").slice(0, 10));
const balanceDate = computed(() => String(frontmatter.value.dataBalanceUpdatedOn || "").slice(0, 10));
const isCategory = computed(() => props.link === "/upgrade" || props.link.startsWith("/upgrade/category/"));
</script>

<template>
    <Callout type="info" class="cp-callout-global-mark" v-if="isUpgrade">
        <template v-if="syncedDate">来源表格同步于 {{ syncedDate }}<template v-if="balanceDate">，另已更新 {{ balanceDate }} 的平衡调整</template>。以下费用和时间为基础值，月卡减免另行计算。</template>
        <template v-else-if="reviewedDate">本页基础属性核对日期：{{ reviewedDate }}；其余资料请参见本页来源。</template>
        <template v-else-if="isCategory">全量数据同步日期：2026-10-13；另已更新 2026-10-20 的平衡调整。往期临时单位的历史数据会单独标注。</template>
        <template v-else>本页保留原项目历史数据，尚未重新核对当前来源；不能视为最新版本数据。</template>
    </Callout>
</template>

<style>
.cp-callout-global-mark { margin: 1rem 0 -0.5rem 0; }
</style>
