---
title: "设置"
module: settings
lastUpdated: null
robots: noindex, nofollow
hasUpdateTime: false
---

<script>
/*
 * 根据月卡减免比例，给出 Option 的 value
 */
function loadGpValueFromDiscount(discount) {
    if (discount === 10) {
        return 1;
    } else if (discount === 15) {
        return 2;
    } else if (discount === 20) {
        return 3;
    }
    return 0;
}

/**
 * 根据 option 的 value 值确定月卡减免比例
 */
function getDiscountFromOptionValue(value) {
    if (value === "1") {
        return "10";
    } else if (value === "2") {
        return "15";
    } else if (value === "3") {
        return "20";
    } else {
        return "0";
    }
}

/*
 * 重置设置
 */
function resetSettings() {
    window.location.reload();
}

/*
 * 保存设置
 */
function saveSettings() {
    // 月卡减免比例的设置
    const gpDiscountTrainingValue = getSelectValue("cp-select-gp-training");
    const gpDiscountTraining = getDiscountFromOptionValue(gpDiscountTrainingValue);

    const gpDiscountResearchValue = getSelectValue("cp-select-gp-research");
    const gpDiscountResearch = getDiscountFromOptionValue(gpDiscountResearchValue);

    const gpDiscountBuildingValue = getSelectValue("cp-select-gp-building");
    const gpDiscountBuilding = getDiscountFromOptionValue(gpDiscountBuildingValue);

    let gpCookieValue;
    if (gpDiscountTraining === "0" && gpDiscountResearch === "0" && gpDiscountBuilding === "0") {
        deleteCookie("cp-gp-discount");
    } else {
        gpCookieValue = gpDiscountTraining + "-" + gpDiscountResearch + "-" + gpDiscountBuilding;
        setCookie("cp-gp-discount", gpCookieValue, "90", "days");
    }

    // 网站主题设置
    const pageThemeValue = getSelectValue("cp-select-page-theme");
    if (pageThemeValue === "1") {
        setCookie("cp-preferred-theme", "light", "10", "years");
    } else if (pageThemeValue === "2") {
        setCookie("cp-preferred-theme", "dark", "10", "years");
    } else {
        deleteCookie("cp-preferred-theme");
    }

    // 弹出提示信息
    generateToast("设置保存成功", {
        type: "success",
        showDuration: 3000
    });
}
</script>

<script setup>
import { inBrowser } from "vitepress";
import SelectContainer from "@/components/select/SelectContainer.vue";
import Select, { getSelectValue, setSelectValue } from "@/components/select/Select.vue";
import Option from "@/components/select/Option.vue";
import { generateToast } from "@/components/dialog/Toast.vue";
import { getCookie, setCookie, deleteCookie, isNumber } from "@/assets/global/utils.js";

/*
 * 获取三个月卡减免比例
 */
const gpCookieValue = inBrowser ? getCookie("cp-gp-discount") : null;
let gpTrainingActiveValue = 0;
let gpResearchActiveValue = 0;
let gpBuildingActiveValue = 0;
// 如果 cookie 不存在，则认为没有减免比例，不进行任何操作
if (gpCookieValue) {
    // 月卡的数组长度一定是 3，如果不是则使用默认值
    let gpDiscountArr = gpCookieValue.split("-");
    if (gpDiscountArr.length !== 3) {
        gpDiscountArr = [0,0,0];
    }
    const gpDiscountTraining = parseInt(gpDiscountArr[0]);
    const gpDiscountResearch = parseInt(gpDiscountArr[1]);
    const gpDiscountBuilding = parseInt(gpDiscountArr[2]);
    gpTrainingActiveValue = loadGpValueFromDiscount(gpDiscountTraining);
    gpResearchActiveValue = loadGpValueFromDiscount(gpDiscountResearch);
    gpBuildingActiveValue = loadGpValueFromDiscount(gpDiscountBuilding);
}

/*
 * 加载用户当前的主题
 */
const preferredTheme = inBrowser ? getCookie("cp-preferred-theme") : null;
let pageThemeActiveValue = 0;
if (preferredTheme) {
    if (preferredTheme === "light") {
        pageThemeActiveValue = 1;
    } else if (preferredTheme === "dark") {
        pageThemeActiveValue = 2;
    }
}

</script>

网站的所有设置都需要重新刷新页面后才可生效。

## 月卡减免比例

在这个区域，你可以单独设置月卡的训练、研究和建筑加成。月卡减免比例的设置均保留 90 天。

<SelectContainer title="训练加成" selectId="cp-select-gp-training" aria-label="训练加成下拉菜单"
    :activeValue="gpTrainingActiveValue" selectWidth="12rem">
    <Option text="无" value="0" />
    <Option text="10%" value="1" />
    <Option text="15%" value="2" />
    <Option text="20%" value="3" />
</SelectContainer>
<SelectContainer title="研究加成" selectId="cp-select-gp-research" aria-label="研究加成下拉菜单"
    :activeValue="gpResearchActiveValue" selectWidth="12rem">
    <Option text="无" value="0" />
    <Option text="10%" value="1" />
    <Option text="15%" value="2" />
    <Option text="20%" value="3" />
</SelectContainer>
<SelectContainer title="建造加成" selectId="cp-select-gp-building" aria-label="建造加成下拉菜单"
    :activeValue="gpBuildingActiveValue" selectWidth="12rem">
    <Option text="无" value="0" />
    <Option text="10%" value="1" />
    <Option text="15%" value="2" />
    <Option text="20%" value="3" />
</SelectContainer>

## 网站主题

<SelectContainer title="切换网站主题" selectId="cp-select-page-theme" aria-label="切换网站主题的下拉菜单"
    :activeValue="pageThemeActiveValue" selectWidth="12rem">
    <Option text="跟随系统（默认）" value="0" />
    <Option text="始终使用浅色主题" value="1" />
    <Option text="始终使用深色主题" value="2" />
</SelectContainer>

<hr class="cp-light-row-division" />

## 搜索

右上角搜索按单位名称、简称和英文名称查询本地升级资料，无需设置搜索服务。

<hr class="cp-light-row-division" />

<div class="cp-settings-operation-btn">
    <button class="btn-secondary" @click="resetSettings">重置</button>
    <button class="btn-primary" @click="saveSettings">保存</button>
</div>

<style lang="scss">
.cp-settings-operation-btn {
    display: flex;
    justify-content: space-between;

    button {
        width: 5rem;
    }
}
</style>