function confirmDelete(id){
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podras revertir este cambio!!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, borralo!',
        cancelButtonText: 'Noo :(',
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Borrado!!',
            'El insumo fue eliminado.',
            'success'
          ).then(function(){
              window.location.href = "/eliminar_insumos/"+id+"/";
          })
        }
})}