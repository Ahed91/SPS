// test 
function test(){
alert('ahed')
}
$(document).ready(function() {

var myInterval = setInterval(function(){
    $.ajax({
          url:document.URL + "A1"
           }).success (function(responseText) {
           $("#A1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "A2"
           }).success (function(responseText) {
           $("#A2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "A3"
           }).success (function(responseText) {
           $("#A3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "A4"
           }).success (function(responseText) {
           $("#A4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "B1"
           }).success (function(responseText) {
           $("#B1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "B2"
           }).success (function(responseText) {
           $("#B2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "B3"
           }).success (function(responseText) {
           $("#B3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "B4"
           }).success (function(responseText) {
           $("#B4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "C1"
           }).success (function(responseText) {
           $("#C1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "C2"
           }).success (function(responseText) {
           $("#C2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "C3"
           }).success (function(responseText) {
           $("#C3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "C4"
           }).success (function(responseText) {
           $("#C4").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "D1"
           }).success (function(responseText) {
           $("#D1").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "D2"
           }).success (function(responseText) {
           $("#D2").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "D3"
           }).success (function(responseText) {
           $("#D3").attr('src',responseText+'.png')
           })

    $.ajax({
          url:document.URL + "D4"
           }).success (function(responseText) {
           $("#D4").attr('src',responseText+'.png')
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
                '    <div class="w2ui-field">'+
                '        <label>Note :</label>'+
                '        <div>'+
                '           <textarea name="note" rows="4" style="width: 250px"></textarea>'+
                '        </div>'+
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
        });
    }
    $().w2popup('open', {
        title   : 'Reserve a Location',
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
                $('#w2ui-popup #form').w2render('reserve');
                w2ui['reserve'].record['location'] = loc; 
                w2ui['reserve'].refresh();
            }
        }
    });
}
