// test 
function test(){
alert('ahed')
}
$(document).ready(function() {
    
  $('#background').css('width',$(window).width())
  $('#background').css('height',$(window).height())
  $('#A1').css('left',parseInt($('#A1').css('left').replace('px',''))*$(window).width()/1527)
  $('#A2').css('left',parseInt($('#A2').css('left').replace('px',''))*$(window).width()/1527)
  $('#A3').css('left',parseInt($('#A3').css('left').replace('px',''))*$(window).width()/1527)
  $('#A4').css('left',parseInt($('#A4').css('left').replace('px',''))*$(window).width()/1527)
  $('#C1').css('left',parseInt($('#C1').css('left').replace('px',''))*$(window).width()/1527)
  $('#C2').css('left',parseInt($('#C2').css('left').replace('px',''))*$(window).width()/1527)
  $('#C3').css('left',parseInt($('#C3').css('left').replace('px',''))*$(window).width()/1527)
  $('#C4').css('left',parseInt($('#C4').css('left').replace('px',''))*$(window).width()/1527)
  $('#B1').css('left',parseInt($('#B1').css('left').replace('px',''))*$(window).width()/1527)
  $('#B2').css('left',parseInt($('#B2').css('left').replace('px',''))*$(window).width()/1527)
  $('#B3').css('left',parseInt($('#B3').css('left').replace('px',''))*$(window).width()/1527)
  $('#B4').css('left',parseInt($('#B4').css('left').replace('px',''))*$(window).width()/1527)
  $('#D1').css('left',parseInt($('#D1').css('left').replace('px',''))*$(window).width()/1527)
  $('#D2').css('left',parseInt($('#D2').css('left').replace('px',''))*$(window).width()/1527)
  $('#D3').css('left',parseInt($('#D3').css('left').replace('px',''))*$(window).width()/1527)
  $('#D4').css('left',parseInt($('#D4').css('left').replace('px',''))*$(window).width()/1527)
  $('#E1').css('left',parseInt($('#E1').css('left').replace('px',''))*$(window).width()/1527)
  $('#E2').css('left',parseInt($('#E2').css('left').replace('px',''))*$(window).width()/1527)
  $('#E3').css('left',parseInt($('#E3').css('left').replace('px',''))*$(window).width()/1527)
  $('#E4').css('left',parseInt($('#E4').css('left').replace('px',''))*$(window).width()/1527)
  $('#F1').css('left',parseInt($('#F1').css('left').replace('px',''))*$(window).width()/1527)
  $('#F2').css('left',parseInt($('#F2').css('left').replace('px',''))*$(window).width()/1527)
  $('#F3').css('left',parseInt($('#F3').css('left').replace('px',''))*$(window).width()/1527)
  $('#F4').css('left',parseInt($('#F4').css('left').replace('px',''))*$(window).width()/1527)
  $('#A1').css('top',parseInt($('#A1').css('top').replace('px',''))*$(window).height()/1143)
  $('#A2').css('top',parseInt($('#A2').css('top').replace('px',''))*$(window).height()/1143)
  $('#A3').css('top',parseInt($('#A3').css('top').replace('px',''))*$(window).height()/1143)
  $('#A4').css('top',parseInt($('#A4').css('top').replace('px',''))*$(window).height()/1143)
  $('#C1').css('top',parseInt($('#C1').css('top').replace('px',''))*$(window).height()/1143)
  $('#C2').css('top',parseInt($('#C2').css('top').replace('px',''))*$(window).height()/1143)
  $('#C3').css('top',parseInt($('#C3').css('top').replace('px',''))*$(window).height()/1143)
  $('#C4').css('top',parseInt($('#C4').css('top').replace('px',''))*$(window).height()/1143)
  $('#B1').css('top',parseInt($('#B1').css('top').replace('px',''))*$(window).height()/1143)
  $('#B2').css('top',parseInt($('#B2').css('top').replace('px',''))*$(window).height()/1143)
  $('#B3').css('top',parseInt($('#B3').css('top').replace('px',''))*$(window).height()/1143)
  $('#B4').css('top',parseInt($('#B4').css('top').replace('px',''))*$(window).height()/1143)
  $('#D1').css('top',parseInt($('#D1').css('top').replace('px',''))*$(window).height()/1143)
  $('#D2').css('top',parseInt($('#D2').css('top').replace('px',''))*$(window).height()/1143)
  $('#D3').css('top',parseInt($('#D3').css('top').replace('px',''))*$(window).height()/1143)
  $('#D4').css('top',parseInt($('#D4').css('top').replace('px',''))*$(window).height()/1143)
  $('#E1').css('top',parseInt($('#E1').css('top').replace('px',''))*$(window).height()/1143)
  $('#E2').css('top',parseInt($('#E2').css('top').replace('px',''))*$(window).height()/1143)
  $('#E3').css('top',parseInt($('#E3').css('top').replace('px',''))*$(window).height()/1143)
  $('#E4').css('top',parseInt($('#E4').css('top').replace('px',''))*$(window).height()/1143)
  $('#F1').css('top',parseInt($('#F1').css('top').replace('px',''))*$(window).height()/1143)
  $('#F2').css('top',parseInt($('#F2').css('top').replace('px',''))*$(window).height()/1143)
  $('#F3').css('top',parseInt($('#F3').css('top').replace('px',''))*$(window).height()/1143)
  $('#F4').css('top',parseInt($('#F4').css('top').replace('px',''))*$(window).height()/1143)
  $('.indicator').css('width', (Math.max(29*$(window).width()/1527, 29*$(window).height()/1143)+Math.max(29*$(window).width()/1527, 29*$(window).height()/1143))/2)
  $('.indicator').css('height', (Math.max(29*$(window).width()/1527, 29*$(window).height()/1143)+Math.max(29*$(window).width()/1527, 29*$(window).height()/1143))/2)
  $('#contact_icon').css('left',parseInt($('#contact_icon').css('left').replace('px',''))*$(window).width()/1527)
  $('#contact_icon').css('top',parseInt($('#contact_icon').css('top').replace('px',''))*$(window).height()/1143)
  $('#contact_icon').css('width',parseInt($('#contact_icon').css('width').replace('px',''))*$(window).width()/1527)



  var myInterval = setInterval(function(){
    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "A1"
           }).success (function(responseText) {
           $("#A1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "A2"
           }).success (function(responseText) {
           $("#A2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "A3"
           }).success (function(responseText) {
           $("#A3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "A4"
           }).success (function(responseText) {
           $("#A4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "B1"
           }).success (function(responseText) {
           $("#B1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "B2"
           }).success (function(responseText) {
           $("#B2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "B3"
           }).success (function(responseText) {
           $("#B3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "B4"
           }).success (function(responseText) {
           $("#B4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "C1"
           }).success (function(responseText) {
           $("#C1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "C2"
           }).success (function(responseText) {
           $("#C2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "C3"
           }).success (function(responseText) {
           $("#C3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "C4"
           }).success (function(responseText) {
           $("#C4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "D1"
           }).success (function(responseText) {
           $("#D1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "D2"
           }).success (function(responseText) {
           $("#D2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "D3"
           }).success (function(responseText) {
           $("#D3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "D4"
           }).success (function(responseText) {
           $("#D4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "E1"
           }).success (function(responseText) {
           $("#E1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "E2"
           }).success (function(responseText) {
           $("#E2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "E3"
           }).success (function(responseText) {
           $("#E3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "E4"
           }).success (function(responseText) {
           $("#E4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "F1"
           }).success (function(responseText) {
           $("#F1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "F2"
           }).success (function(responseText) {
           $("#F2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "F3"
           }).success (function(responseText) {
           $("#F3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL.replace('main','') + "?location="  + "F4"
           }).success (function(responseText) {
           $("#F4").attr('src',responseText+'.png')
           })

           },10000)
});

function contact () {
    if (!w2ui.contact) {
        $().w2form({
            name: 'contact',
            style: 'border: 0px; background-color: transparent;',
            formHTML: 
                '<div class="w2ui-page page-0">'+
                '    <div class="w2ui-field">'+
                '        <label>First Name:</label>'+
                '        <div>'+
                '           <input name="first_name" type="text" maxlength="100" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>Last Name:</label>'+
                '        <div>'+
                '            <input name="last_name" type="text" maxlength="100" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>Email:</label>'+
                '        <div>'+
                '            <input name="email" type="text" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>body :</label>'+
                '        <div>'+
                '           <textarea name="body" rows="4" style="width: 250px"></textarea>'+
                '        </div>'+
                '    </div>'+
                '</div>'+
                '<div class="w2ui-buttons">'+
                '    <button class="btn" name="reset">Reset</button>'+
                '    <button class="btn" name="save">Save</button>'+
                '</div>',
            fields: [
                { field: 'first_name', type: 'text', required: true },
                { field: 'last_name', type: 'text', required: true },
                { field: 'email', type: 'email' },
                { field: 'body', type: 'text' },
            ],
            record: { 
                first_name    : 'Ahed',
                last_name     : 'Eid',
                email         : 'Ahed@email.com',
                body          : 'sample text sample text sample text sample text sample text sample text sample text'
            },
            actions: {
                "save": function () { 
                    $.ajax({
                          url:document.location['origin']+'/contact/'+$('input#first_name').val()+'/'+$('input#last_name').val()+'/'+$('input#email').val()+'/'+$('textarea#body').val()
                            
                    }).success (function(responseText) {
                           alert(responseText)
                    })
                },
                "reset": function () { this.clear(); },
            }
        });
    }
    $().w2popup('open', {
        title   : 'Contact Us',
        body    : '<div id="form" style="width: 100%; height: 100%;"></div>',
        style   : 'padding: 15px 0px 0px 0px',
        width   : 500,
        height  : 300, 
        showMax : true,
        onToggle: function (event) {
            $(w2ui.contact.box).hide();
            event.onComplete = function () {
                $(w2ui.contact.box).show();
                w2ui.contact.resize();
            }
        },
        onOpen: function (event) {
            event.onComplete = function () {
                // specifying an onOpen handler instead is equivalent to specifying an onBeforeOpen handler, which would make this code execute too early and hence not deliver.
                $('#w2ui-popup #form').w2render('contact');
            }
        }
    });
}


function reserve(loc) {
    if (!w2ui.reserve) {
        $().w2form({
            name: 'reserve',
            style: 'border: 0px; background-color: transparent;',
            formHTML: 
                '<div class="w2ui-page page-0">'+
                '    <div class="w2ui-field">'+
                '        <label>Name :</label>'+
                '        <div>'+
                '           <input name="username" type="text" maxlength="100" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>Location:</label>'+
                '        <div>'+
                '           <input name="location" type="text" maxlength="2" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>Date:</label>'+
                '        <div>'+
                '            <input name="date" type="date" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>Start Time:</label>'+
                '        <div>'+
                '            <input name="timefrom" type="time" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field">'+
                '        <label>End Time:</label>'+
                '        <div>'+
                '            <input name="timeto" type="time" style="width: 250px"/>'+
                '        </div>'+
                '    </div>'+
                '    <div class="w2ui-field" id="div_chart">'+
                '        <label>Note :</label>'+
                '        <div>'+
                '           <textarea name="note" rows="4" style="width: 250px"></textarea>'+
                '        </div>'+
                '        <canvas id="myChart" width="400" height="400"></canvas> '+
                '    </div>'+
                '</div>'+
                '<div class="w2ui-buttons">'+
                '    <button class="btn" name="reset">Reset</button>'+
                '    <button class="btn" name="save">Save</button>'+
                '</div>',
            fields: [
                { field: 'username', type: 'text', required: true },
                { field: 'location', type: 'text', required: true },
                { field: 'date', type: 'date',  options  : {
                        format: 'd.m.yyyy',
                        start : new Date().getDate()+'.'+(new Date().getMonth()+1)+'.'+new Date().getFullYear(),
                        end : new Date().getDate()+'.'+(new Date().getMonth()+1)+'.'+(new Date().getFullYear()+1)
                                                           }
                },
                { field: 'timefrom', type: 'time', options: { format: 'h24', start:new Date().getHours()+':00' }},
                { field: 'timeto', type: 'time', options: { format: 'h24', start:new Date().getHours()+':00' }},
                { field: 'note', type: 'text' },
            ],
            record: { 
                username : 'Ahed',
                location : loc,
                date     : new Date().getDate()+'.'+(new Date().getMonth()+1)+'.'+new Date().getFullYear(),
                timefrom         : new Date().getHours()+':00',
                timeto         : new Date().getHours()+':00',
                note          : 'Anything else'
            },
            actions: {
                "save": function () { 
                    $.ajax({
                          url:document.location['origin']+'/reserve/'+$('input#username').val()+'/'+$('input#location').val()+'/'+$('input#date').val()+'/'+$('input#timefrom').val()+'/'+$('input#timeto').val()+'/'+$('textarea#note').val()
                            
                    }).success (function(responseText) {
                           alert(responseText)
                       })
                },
                "reset": function () { this.clear() },
            },
            onChange: function(event){
                if (event.target ==  'timefrom'){
                    myRe = /^[0-9][0-9]:[0-9][0-9]$/
                    if (myRe.test(event.value_new)){
                       timefrom_hour = event.value_new.split(':')[0];
                       $.ajax({
                           url:document.URL.replace('main','') + "get_data_for_chart?location=" + loc + '&hour=' + timefrom_hour 
                       }).success (function(responseText) {
                           $('#myChart').remove()
                           $('#div_chart').append('<canvas id="myChart" width="400" height="400"></canvas>')
                           eval(responseText)
                           draw_chart()
                           })
                    } 
                }
            }
        });
    }
    $().w2popup('open', {
        title   : 'Reserve a Location',
        body    : '<div id="form" style="width: 100%; height: 100%;"></div>',
        style   : 'padding: 15px 0px 0px 0px',
        width   : 450,
        height  : 600, 
        showMax : true,
        onToggle: function (event) {
            $(w2ui.contact.box).hide();
            event.onComplete = function () {
                $(w2ui.contact.box).show();
                w2ui.contact.resize();
            }
        },
        onOpen: function (event) {
            event.onComplete = function () {
                // specifying an onOpen handler instead is equivalent to specifying an onBeforeOpen handler, which would make this code execute too early and hence not deliver.
                $('#w2ui-popup #form').w2render('reserve');
                w2ui['reserve'].record['location'] = loc; 
                w2ui['reserve'].refresh();
                $.ajax({
                     url:document.URL.replace('main','') + "get_data_for_chart?location=" + loc + '&hour='+ new Date().getHours()
                }).success (function(responseText) {
                      $('#myChart').remove()
                      $('#div_chart').append('<canvas id="myChart" width="400" height="400"></canvas>')
                      eval(responseText)
                      draw_chart()
                })
                draw_chart()

            }
        },
    });
}

function draw_chart(hour) {
var ctx = document.getElementById("myChart").getContext("2d");
myDoughnutChart = new Chart(ctx).Doughnut(data);
}

var data = [
{
    value: 60,
    color: "#949FB1",
    highlight: "#A8B3C5",
    label: "Empty"
                                            
},
{
    value: 0,
    color: "#46BFBD",
    highlight: "#5AD3D1",
    label: "Reserved"
                                            
},
]

