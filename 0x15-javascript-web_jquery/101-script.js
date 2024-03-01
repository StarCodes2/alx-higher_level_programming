// Adds, removes and clears LI elements from a list when the user clicks
$(document).ready(function () {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', () => {
    const children = $('UL.my_list').children();
    if (children.length > 0) {
      children.last().remove();
    }
  });

  $('DIV#clear_list').on('click', () => {
    const myList = $('UL.my_list');
    if (myList.length > 0) {
      myList.empty();
    }
  })
});
