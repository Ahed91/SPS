jQuery(document).ready(function($){
	    $form_modal = $('.cd-user-modal'),
		$form_login = $form_modal.find('#cd-login'),
		$form_signup = $form_modal.find('#cd-signup'),
		$form_forgot_password = $form_modal.find('#cd-reset-password'),
		$form_modal_tab = $('.cd-switcher'),
		$tab_login = $form_modal_tab.children('li').eq(0).children('a'),
		$tab_signup = $form_modal_tab.children('li').eq(1).children('a'),
		$forgot_password_link = $form_login.find('.cd-form-bottom-message a'),
		$back_to_login_link = $form_forgot_password.find('.cd-form-bottom-message a'),
		$main_nav = $('.main-nav'),
        email_error = $form_modal.find('span').eq(0),
        password_error = $form_modal.find('span').eq(1),
        username_error = $form_modal.find('span').eq(2),
        email_sign_error = $form_modal.find('span').eq(3),
        password_sign_error = $form_modal.find('span').eq(4),
        mobile_error = $form_modal.find('span').eq(5),
        terms_error = $form_modal.find('span').eq(6);
        email_forget_error = $form_modal.find('span').eq(7);

	//open modal
	$main_nav.on('click', function(event){

		if( $(event.target).is($main_nav) ) {
			// on mobile open the submenu
			$(this).children('ul').toggleClass('is-visible');
		} else {
			// on mobile close submenu
			$main_nav.children('ul').removeClass('is-visible');
			//show modal layer
			$form_modal.addClass('is-visible');	
			//show the selected form
			( $(event.target).is('.cd-signup') ) ? signup_selected() : login_selected();
		}

	});

	//close modal
	$('.cd-user-modal').on('click', function(event){
		if( $(event.target).is($form_modal) || $(event.target).is('.cd-close-form') ) {
			$form_modal.removeClass('is-visible');
		}	
	});
	//close modal when clicking the esc keyboard button
	$(document).keyup(function(event){
    	if(event.which=='27'){
    		$form_modal.removeClass('is-visible');
	    }
    });

	//switch from a tab to another
	$form_modal_tab.on('click', function(event) {
		event.preventDefault();
		( $(event.target).is( $tab_login ) ) ? login_selected() : signup_selected();
	});

	//hide or show password
	$('.hide-password').on('click', function(){
		var $this= $(this),
			$password_field = $this.prev('input');
		
		( 'password' == $password_field.attr('type') ) ? $password_field.attr('type', 'text') : $password_field.attr('type', 'password');
		( 'Hide' == $this.text() ) ? $this.text('Show') : $this.text('Hide');
		//focus and move cursor to the end of input field
		$password_field.putCursorAtEnd();
	});

	//show forgot-password form 
	$forgot_password_link.on('click', function(event){
		event.preventDefault();
		forgot_password_selected();
	});

	//back to login from the forgot-password form
	$back_to_login_link.on('click', function(event){
		event.preventDefault();
		login_selected();
	});
    // on focus hide errors
    $form_login.find('input[name="email"]').bind('focus',function(){
        email_error.removeClass('is-visible')
    });
    $form_login.find('input[name="password"]').bind('focus',function(){
        password_error.removeClass('is-visible')
    });
    $form_signup.find('input[name="username"]').bind('focus',function(){
        username_error.removeClass('is-visible')
    });
    $form_signup.find('input[name="email"]').bind('focus',function(){
        email_sign_error.removeClass('is-visible')
    });
    $form_signup.find('input[name="password"]').bind('focus',function(){
        password_sign_error.removeClass('is-visible')
    });
    $form_signup.find('input[name="mobile"]').bind('focus',function(){
        mobile_error.removeClass('is-visible')
    });
    $form_signup.find('input[name="username"]').bind('focus',function(){
        username_error.removeClass('is-visible')
    });
    $form_signup.find('input[type="checkbox"]').bind('click',function(){
        terms_error.removeClass('is-visible')
    });
    $form_forgot_password.find('input[type="email"]').bind('focus',function(){
        email_forget_error.removeClass('is-visible')
    });
	function login_selected(){
		$form_login.addClass('is-selected');
		$form_signup.removeClass('is-selected');
		$form_forgot_password.removeClass('is-selected');
		$tab_login.addClass('selected');
		$tab_signup.removeClass('selected');
	}

	function signup_selected(){
		$form_login.removeClass('is-selected');
		$form_signup.addClass('is-selected');
		$form_forgot_password.removeClass('is-selected');
		$tab_login.removeClass('selected');
		$tab_signup.addClass('selected');
	}

	function forgot_password_selected(){
		$form_login.removeClass('is-selected');
		$form_signup.removeClass('is-selected');
		$form_forgot_password.addClass('is-selected');
	}

	$form_login.find('input[type="submit"]').on('click', function(event){
		event.preventDefault();
        re_email = /^([a-z]{1,5}[.]{0,1}[0-9]{0,5}){1,20}@([a-z]{1,5}[0-9]{0,5}){1,20}[.](com|org|net|ps)$/
        re_password = /^.{6,20}$/
        var email = $form_login.find('input[name=email]')
        var password = $form_login.find('input[name=password]')
        var send_login_details = true
        if (!re_email.test(email.val())){
            send_login_details = false
            email_error.addClass('is-visible')
            email_error.text('Please enter a valid email address')
        }
        if (!re_password.test(password.val())){
            send_login_details = false
            password_error.addClass('is-visible')
        }
        if (send_login_details){
            $.ajax({
              url:document.location['origin'] + "/login?email="  + email.val() + "&password=" + password.val()
            }).success (function(responseText) {
                 if (responseText == "Done")
                   window.open(document.location['origin'] + '/main', '_self')
                 else if (responseText == "Please Sign up"){
                   email_error.text('Please Sign up before login')
                   email_error.addClass('is-visible')}
            });
        }
	});
	$form_signup.find('input[type="submit"]').on('click', function(event){
		event.preventDefault();
        re_email = /^([a-z]{1,5}[.]{0,1}[0-9]{0,5}){1,20}@([a-z]{1,5}[0-9]{0,5}){1,20}[.](com|org|net|ps)$/
        re_password = /^.{6,20}$/
        re_username = /^([a-z]{1,5}[0-9]{0,5}){1,20}$/
        re_mobile = /^([0-9]{7,20}|[+][0-9]{12,20})$/
        var username  = $form_signup.find('input[name=username]')
        var email = $form_signup.find('input[name=email]')
        var password = $form_signup.find('input[name=password]')
        var mobile = $form_signup.find('input[name=mobile]')
        var send_signup_details = true
        var is_terms_accepted = $('#accept-terms').prop('checked')
        if (!re_username.test(username.val())){
            send_signup_details = false
            username_error.addClass('is-visible')
            username_error.text('Please enter a valid username which is begin with a letter , the letters are lower case and numbers')}
        if (!re_email.test(email.val())){
            send_signup_details = false
            email_sign_error.addClass('is-visible')
            email_sign_error.text('Please enter a valid email')}
        if (!re_password.test(password.val())){
            send_signup_details = false
            password_sign_error.addClass('is-visible')}
        if (!re_mobile.test(mobile.val())){
            send_signup_details = false
            mobile_error.addClass('is-visible')}
        if (!is_terms_accepted){
            send_signup_details = false
            terms_error.addClass('is-visible')}
        if (send_signup_details){
            $.ajax({
              url:document.location['origin'] + "/signup?email="  + email.val() + "&password=" + password.val() + '&username=' + username.val() + '&mobile=' + mobile.val()
            }).success (function(responseText) {
                 if (responseText == "Done")
                   window.open(document.location['origin'] + '/sign', '_self')
                 else if (responseText == "username_error"){
                   username_error.text('Please choose another username')
                   username_error.addClass('is-visible')}
                 else if (responseText == "email_error"){
                   email_sign_error.text('Please choose another email')
                   email_sign_error.addClass('is-visible')}
            });
        }
	});
	$form_forgot_password.find('input[type="submit"]').on('click', function(event){
		event.preventDefault();
        re_email = /^([a-z]{1,5}[.]{0,1}[0-9]{0,5}){1,20}@([a-z]{1,5}[0-9]{0,5}){1,20}[.](com|org|net|ps)$/
        var email = $form_forgot_password.find('input[type=email]')
        var send_forget_details = true
        if (!re_email.test(email.val())){
            send_forget_details = false
            email_forget_error.addClass('is-visible')
        }
        if (send_forget_details){
            console.log('not implemented')
        }
	});

	//IE9 placeholder fallback
	//credits http://www.hagenburger.net/BLOG/HTML5-Input-Placeholder-Fix-With-jQuery.html
	if(!Modernizr.input.placeholder){
		$('[placeholder]').focus(function() {
			var input = $(this);
			if (input.val() == input.attr('placeholder')) {
				input.val('');
		  	}
		}).blur(function() {
		 	var input = $(this);
		  	if (input.val() == '' || input.val() == input.attr('placeholder')) {
				input.val(input.attr('placeholder'));
		  	}
		}).blur();
		$('[placeholder]').parents('form').submit(function() {
		  	$(this).find('[placeholder]').each(function() {
				var input = $(this);
				if (input.val() == input.attr('placeholder')) {
			 		input.val('');
				}
		  	})
		});
	}

});


//credits http://css-tricks.com/snippets/jquery/move-cursor-to-end-of-textarea-or-input/
jQuery.fn.putCursorAtEnd = function() {
	return this.each(function() {
    	// If this function exists...
    	if (this.setSelectionRange) {
      		// ... then use it (Doesn't work in IE)
      		// Double the length because Opera is inconsistent about whether a carriage return is one character or two. Sigh.
      		var len = $(this).val().length * 2;
      		this.setSelectionRange(len, len);
    	} else {
    		// ... otherwise replace the contents with itself
    		// (Doesn't work in Google Chrome)
      		$(this).val($(this).val());
    	}
	});
};
