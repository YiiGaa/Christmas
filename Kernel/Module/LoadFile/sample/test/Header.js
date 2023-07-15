/********************
    @Describe: Header v1.0
    @Param: param = [*]
    @Return: null
    @BeCareful:
********************/ 
/*@@@@@@123@@@@@@*/

function ControlHeader(params) {
    var ModuleId = {
        "bodyId":"#id_Header_body"
    }
    var Config = {
        "selectCallBackFunction":params["selectCallBackFunction"],
        "searchCallBackFunction":params["searchCallBackFunction"],
        "languageCallBackFunction":params["languageCallBackFunction"]
    }

    var VueObject_Body;
    this.initialize = function(){
        try {
            VueObject_Body = new Vue({
                el:ModuleId["bodyId"],
                data:{
                    Vue_Header_Logo:params["logo"],
                    Vue_Header_LogoLink:params["logoLink"],
                    Vue_Header_ActiveLink:params["linkActive"],
                    Vue_Header_Link:params["link"],
                    Vue_Header_Search:params["search"],
                    Vue_Header_Language:params["language"],

                    Vue_Header_SearchText:""
                },
                methods:{
                    Vue_Header_SelectFunction: function (data, title) {
                        this.Vue_Header_ActiveLink = title
                        try {bootstrap.Collapse.getInstance(document.getElementById('id_Header_navbar')).hide()} catch (error) { }
                        NotifyCallBackFunction("selectCallBackFunction", data)
                    },
                    Vue_Header_SearchFunction: function (data) {
                        if(this.Vue_Header_SearchText!=""){
                            try {bootstrap.Collapse.getInstance(document.getElementById('id_Header_navbar')).hide()} catch (error) { }
                            NotifyCallBackFunction("searchCallBackFunction", this.Vue_Header_SearchText)
                        }
                    },
                    Vue_Header_LanguageFunction: function (data) {
                        try {bootstrap.Collapse.getInstance(document.getElementById('id_Header_navbar')).hide()} catch (error) { }
                        NotifyCallBackFunction("languageCallBackFunction", data)
                    }
                }
            });
        } catch (e) {
            console.log("Header exception.");
            console.log(e);
        }
    };

    var NotifyCallBackFunction = function(key, data) {
        var notify = Config[key]
        if (notify) {
            notify(data)
        }
    }

    this.UpdateNew = function(data){
        if(data["linkActive"]){
            VueObject_Body.Vue_Header_ActiveLink = data["linkActive"];
        }
    }


}

/*@@@@@@module@@@@@@*/

/**Loading Common Lib**/
var ControlLoad = function(){
    lib_Load('../../Common/Lib/', ControlInit);
}

/**The following code is the test code**/
var testfunction = function(data){
    console.log(data)
}

var Header;
var ControlInit = function(){
    var HeaderInfo = {
        "logo":"./test/logo.svg",                                                   //logo
        "logoLink":"https://stoprefactoring.com/",                                  //logo跳转地址，a标签跳转
        "linkActive":"导航1",                                                        //初始激活的导航title
        "link":[                                                                    //导航设置
            {"title":"导航1", "link":"https://stoprefactoring.com/"},                //单个导航设置，link是a标签跳转
            {"title":"导航2", "link":""},                                            //如果不需要跳转或只需要触发回调函数selectCallBackFunction，则这里设置为空字符串
            {"title":"下拉导航", "list":[                                             //设置下拉菜单
                {"title":"下拉导航1", "link":"#link"},                                //设置子下拉导航                           
                {"title":"下拉导航2", "link":"https://stoprefactoring.com/"}   
            ]}
        ],
        "search":{
            "placeholder":"输入关键字后请按Enter键"                                     //设置搜索提示语，回车键触发回调函数searchCallBackFunction
        },
        "language":{
            "title":"语言",                                                          //右边菜单名称
            "list":[
                {"title":"中文", "link":"https://stoprefactoring.com/"},             //下拉菜单设置
                {"title":"日文", "link":""}                                          //如果不需要跳转或只需要触发回调函数languageCallBackFunction，则这里设置为空字符串
            ]
        },
        "selectCallBackFunction":testfunction,                                       //导航回调函数selectCallBackFunction，可缺省
        "searchCallBackFunction":testfunction,                                       //搜索回调函数searchCallBackFunction，可缺省
        "languageCallBackFunction":testfunction                                      //右边菜单回调函数languageCallBackFunction，可缺省
    };
    Header = new ControlHeader(HeaderInfo);
    Header.initialize();                                                             //调用初始化方法

    // var HeaderUpdate = {
    //     "linkActive":"需要激活的导航"                                                //设置激活的导航，设置导航title
    // }
    // Header.UpdateNew(HeaderUpdate);                                               //调用更新方法
}
