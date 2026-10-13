<script setup>
import { computed } from "vue";
import UnitTable from "./UnitTable.vue";
import { imagePlaceholder } from "@/assets/local-images.js";
import { dataLabel } from "@/assets/data-labels.js";

const props = defineProps({ data: { type: Object, required: true } });
const images = computed(() => props.data.images.filter(image => image.localPath));
const sortedTables = computed(() => props.data.tables.map((table, index) => ({ ...table, index })).sort((a, b) => {
    const score = table => table.headers.some(header => /Cost|Build Time|Upgrade Time|Research Time/.test(header)) ? 0 : 1;
    return score(a) - score(b) || a.index - b.index;
}));
const history = computed(() => [...props.data.history].sort((a, b) => b.date.localeCompare(a.date)));
const modeNames = {
    "0301-Cannon": ["标准模式", "连发模式"], "0302-Archer-Tower": ["标准模式", "快速模式"],
    "0303-Mortar": ["标准模式", "连发模式"], "030a-Inferno-Tower": ["单头模式", "多头模式"],
    "1102-Archer-Tower": ["长距模式", "短距模式"]
};
function title(table) {
    if (/Charge Level|Supercharge/.test(table.headers[0])) return "蓄能数据";
    if (table.title && !["Statistics", "Common Statistics"].includes(table.title)) return dataLabel(table.title);
    if (table.headers[0] === "Level") {
        const levels = props.data.tables.filter(item => item.headers[0] === "Level");
        const position = levels.findIndex(item => item.sourceTableIndex === table.sourceTableIndex);
        return modeNames[props.data.unitId]?.[position] || "升级数据";
    }
    if (/Level/.test(table.headers[0]) || table.headers[0] === "Number Available") return "等级与数量";
    return "基础属性";
}
function display(cell) {
    if (cell.status === "not_applicable") return "不适用";
    if (cell.status === "unknown") return "未知";
    if (typeof cell.value === "number" && cell.unit !== "seconds") return String(cell.value);
    return cell.displayInput ?? dataLabel(cell.raw);
}
function availabilityBands(table) {
    return /Hall Level/.test(table.headers[0]) && table.rows[0]?.[0]?.raw === "Number Available";
}
function bodyDisplay(table, cell, rowIndex, column) {
    if (availabilityBands(table) && column === 0 && cell.raw === "") {
        return dataLabel(rowIndex % 2 ? table.headers[0] : table.rows[0][0].raw);
    }
    return display(cell);
}
</script>

<template>
    <p class="cp-data-source">
        数据同步：{{ data.sync.syncedOn }} ·
        <a :href="data.sync.revisionUrl" target="_blank" rel="noopener noreferrer">Clash of Clans Wiki</a>
    </p>
    <figure v-if="images.length" class="cp-data-cover">
        <img :src="images[0].localPath || imagePlaceholder" :alt="data.title" />
    </figure>
    <p v-for="notice in data.notices" :key="notice">{{ notice }}</p>
    <template v-if="data.facts?.length">
        <SmallTitle>解锁条件与能力参数</SmallTitle>
        <ul><li v-for="fact in data.facts" :key="fact">{{ fact }}</li></ul>
    </template>
    <Panel v-if="images.length > 1">
        <div class="cp-data-gallery">
            <figure v-for="image in images" :key="image.name">
                <img loading="lazy" class="cp-unit-img" :src="image.localPath" :alt="image.alt" />
                <figcaption>{{ image.alt }}</figcaption>
            </figure>
        </div>
    </Panel>
    <template v-for="table in sortedTables" :key="data.unitId + '-' + table.sourceTableIndex">
        <SmallTitle>{{ title(table) }}</SmallTitle>
        <UnitTable :tableExtraInfo="table.extraInfo">
            <table>
                <thead><tr><th v-for="(header, column) in table.headers" :key="column">{{ dataLabel(header) }}</th></tr></thead>
                <tbody>
                    <tr v-for="(row, index) in table.rows" :key="index">
                        <component :is="availabilityBands(table) && index % 2 ? 'th' : 'td'" v-for="(cell, column) in row" :key="column" :title="cell.status === 'known' ? cell.raw : cell.status === 'unknown' ? '来源没有给出可用数值' : '来源标记为不适用'">{{ bodyDisplay(table, cell, index, column) }}</component>
                    </tr>
                </tbody>
            </table>
        </UnitTable>
    </template>
    <template v-if="history.length">
        <SmallTitle>2026 年更新历史</SmallTitle>
        <ul class="cp-data-history">
            <li v-for="(item, index) in history" :key="index"><strong>{{ item.date }}</strong> {{ item.description }} <a v-if="item.sourceUrl" :href="item.sourceUrl" target="_blank" rel="noopener noreferrer">来源</a></li>
        </ul>
        <p class="cp-data-source">以上为来源记录的变更日期，原文保留供核对；数据同步日期列在页首。</p>
    </template>
</template>

<style lang="scss">
.cp-data-source { color: var(--cp-grey-text-light); font-size: 0.875rem; }
.cp-data-cover { display: flex; justify-content: center; margin: 1rem 0; }
.cp-data-cover img { max-width: min(20rem, 100%); max-height: 16rem; object-fit: contain; }
.cp-data-gallery { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.cp-data-gallery figure { margin: 0; width: 5.5rem; text-align: center; }
.cp-data-gallery img { height: 5.5rem; max-width: 5.5rem; object-fit: contain; }
.cp-data-gallery figcaption { font-size: 0.75rem; line-height: 1.3; overflow-wrap: anywhere; }
.cp-data-history li { margin: 0.75rem 0; }
.cp-theme-dark .cp-data-source { color: var(--cp-grey-text-dark); }
</style>
