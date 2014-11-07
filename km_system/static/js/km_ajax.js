$(document).ready(function(){

console.log('javascript starting');

$('#supplier_list').submit('input[id^=edit-]',function(){
	var supplier_edit_id=$(this).attr('id').split('-')[1];
	console.log(supplier_edit_id);
	edit_post(supplier_edit_id);	
	
});

function edit_post(supplier_edit_id){
	concole.log('edit supplier item is working!')
	if (confirm("Are you need edit this item?")==true){
	$.ajax({
		url:"supplier/change_item/";
		type:"POST";
		data:$("#supplier_item").serialize();
		success:function(json){
			$('#code').val(json.code);
			$('#name').val(json.name);
			$('#address').val(json.address);
			$('#product').val(json.prduct);
			$('#contact').val(json.contact);
			$('#phone').val(json.phone);
			$('#fax').val(json.fax);
			$('#remark').val(json.remark);
			$('#create_by').val(json.create_by);
			$('#create_date').val(json.create_date);
			$('#edit_by').val(json.edit_by);
			$('#edit_date').val(json.edit_date);
			$('#id').val(json.id);
			$('#status').val(json.status);
		};
		error:function(xhr,errmsg,err){
			$("#status"+supplier_edit_id).val("errr");
			console.log(xhr.status+": "+xhr.respnseText);
		};
	});
	}else{
		return false;
	};

};




});






