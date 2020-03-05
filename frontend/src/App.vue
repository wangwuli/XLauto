<template>
    <el-container>
        <el-header>
            <el-menu
                    background-color="#545c64"
                    text-color="#fff"
                    active-text-color="#ffd04b"
                    :default-active="activeIndex"
                    router
                    mode="horizontal"
                    style="overflow-x:auto;"
            >
                <!--                <menutree :data="menu_data"></menutree>-->
                <!--            </el-menu>-->
                <!--            <el-menu>-->
                <NavMenu :navMenus="menuData" style="width:800px;overflow-x:auto;"></NavMenu>
            </el-menu>
        </el-header>

        <el-main>
            <el-tabs v-model="editableTabsValue" type="card" closable @tab-remove="removeTab">
                <el-tab-pane
                        v-for="(item, index) in editableTabs"
                        :key="item.name"
                        :label="item.title"
                        :name="item.name"
                >
                    {{item.content}}
                </el-tab-pane>
            </el-tabs>
        </el-main>

    </el-container>

</template>

<script>
    import NavMenu from "./home/menutree";

    export default {
        components: {
            NavMenu: NavMenu
        },
        data() {
            return {
                menuData: [
                    {
                        //一级
                        entity: {
                            id: 0,
                            name: "aa",
                            icon: "el-icon-message",
                            alias: "一级菜单"
                        }
                    },
                    {
                        //一级
                        entity: {
                            id: 1,
                            name: "systemManage",
                            icon: "el-icon-message",
                            alias: "两级菜单"
                        },
                        //二级
                        childs: [
                            {
                                entity: {
                                    id: 3,
                                    name: "authManage",
                                    icon: "el-icon-loading",
                                    alias: "权限管理",
                                    value: {path: "/hello"}
                                }
                            },
                            {
                                entity: {
                                    id: 4,
                                    name: "roleManage",
                                    icon: "el-icon-bell",
                                    alias: "角色管理",
                                    value: "/system/role"
                                }
                            },
                            {
                                entity: {
                                    id: 2,
                                    name: "menuManage",
                                    icon: "el-icon-edit",
                                    alias: "菜单管理",
                                    value: "/system/menu"
                                }
                            },
                            {
                                entity: {
                                    id: 5,
                                    name: "groupManage",
                                    icon: "el-icon-mobile-phone\r\n",
                                    alias: "分组管理",
                                    value: "/system/group"
                                }
                            }
                        ]
                    },
                    {
                        //一级
                        entity: {
                            id: 6,
                            name: "userManage",
                            icon: "el-icon-news",
                            alias: "三级菜单"
                        },
                        //二级
                        childs: [
                            {
                                entity: {
                                    id: 7,
                                    name: "accountManage",
                                    icon: "el-icon-phone-outline\r\n",
                                    alias: "帐号管理",
                                    value: ""
                                },
                                //三级
                                childs: [
                                    {
                                        entity: {
                                            id: 14,
                                            name: "emailManage",
                                            icon: "el-icon-sold-out\r\n",
                                            alias: "邮箱管理",
                                            value: "/content/email"
                                        }
                                    },
                                    {
                                        entity: {
                                            id: 13,
                                            name: "passManage",
                                            icon: "el-icon-service\r\n",
                                            alias: "密码管理",
                                            value: "/content/pass"
                                        }
                                    }
                                ]
                            },
                            {
                                entity: {
                                    id: 8,
                                    name: "integralManage",
                                    icon: "el-icon-picture",
                                    alias: "积分管理",

                                    value: "/user/integral"
                                }
                            }
                        ]
                    },
                    {
                        //一级
                        entity: {
                            id: 40,

                            name: "contentManage",
                            icon: "el-icon-rank",
                            alias: "四级菜单"
                        },
                        //er级
                        childs: [
                            {
                                entity: {
                                    id: 41,
                                    name: "classifyManage2",
                                    icon: "el-icon-printer",
                                    alias: "分类管理"
                                },
                                //三级
                                childs: [
                                    {
                                        entity: {
                                            id: 42,
                                            name: "classifyManage3",
                                            icon: "el-icon-printer",
                                            alias: "分类管理"
                                        },
                                        //四级
                                        childs: [
                                            {
                                                entity: {
                                                    id: 43,
                                                    name: "classifyManage4",
                                                    icon: "el-icon-printer",
                                                    alias: "分类管理",
                                                    value: "/content/classify"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ],

                editableTabsValue: '2',
                editableTabs: [{
                    title: 'Tab 1',
                    name: '1',
                    content: 'Tab 1 content'
                }, {
                    title: 'Tab 2',
                    name: '2',
                    content: 'Tab 2 content'
                }],
                tabIndex: 2
            }
        },
        methods: {
            addTab(targetName) {
                let newTabName = ++this.tabIndex + '';
                this.editableTabs.push({
                    title: targetName,
                    name: newTabName,
                    content: 'New Tab content'
                });
                this.editableTabsValue = newTabName;
            },
            removeTab(targetName) {
                let tabs = this.editableTabs;
                let activeName = this.editableTabsValue;
                if (activeName === targetName) {
                    tabs.forEach((tab, index) => {
                        if (tab.name === targetName) {
                            let nextTab = tabs[index + 1] || tabs[index - 1];
                            if (nextTab) {
                                activeName = nextTab.name;
                            }
                        }
                    });
                }

                this.editableTabsValue = activeName;
                this.editableTabs = tabs.filter(tab => tab.name !== targetName);
            }
        },
        mounted() {

        }
    }
</script>

<style>
*{
  outline:none;
}
</style>
<!--thanks https://blog.csdn.net/qq_31126175/article/details/81875468-->