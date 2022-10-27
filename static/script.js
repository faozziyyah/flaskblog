$( window ).on("load", function() {

  var darkMode = localStorage.getItem("darkMode");

  const darkModeToggle = $('#first');

  const enableDarkMode = () => {

    $('.second').addClass('seconddark');
    $('.todoheading').addClass('todoheadingdark');
    $('.background').addClass('backgrounddark');
    $('.options').addClass('optionsdark');
    $('.extras').addClass('extrasdark');
    $('.extra').addClass('extradark');
    $('.todolist').addClass('todolistdark');
    $('.th').addClass('thdark');
    $('.td').addClass('tddark');
    $('.addBtn').addClass('addBtndark');
    $('.input').addClass('tododark');
    $('.checked').addClass('checkeddark');
    localStorage.setItem('darkMode', 'enabled');

  }

  const disableDarkMode = () => {

    $('.second').removeClass('seconddark');
    $('.todoheading').removeClass('todoheadingdark');
    $('.background').removeClass('backgrounddark');
    $('.options').removeClass('optionsdark');
    $('.extras').removeClass('extrasdark');
    $('.extra').removeClass('extradark');
    $('.todolist').removeClass('todolistdark');
    $('.th').removeClass('thdark');
    $('.td').removeClass('tddark');
    $('.addBtn').removeClass('addBtndark');
    $('.input').removeClass('tododark');
    $('.checked').removeClass('checkeddark');
    localStorage.setItem('darkMode', null);
    
  }

  if (darkMode === 'enabled') {
    enableDarkMode();
  }

  darkModeToggle.click(function() {

    darkMode = localStorage.getItem('darkMode');
    
    if (darkMode !== 'enabled') {
      enableDarkMode();
    } else {
      disableDarkMode();
    }

  })

});