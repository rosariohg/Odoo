//Importamos React y React Native
import React from 'react';
import { FlatList, Image, StyleSheet, Text, View } from 'react-native';

//Requerimos react-native-odoo para realizar una aplicación entre
//Odoo y React native.
const Odoo = require('react-native-odoo');

//Configuramos Odoo, el host (el cual es nuestra ip), el puerto (8069)
// database, username, password
const odoo = new Odoo({
  host: '192.168.43.172',
  port: 8069,
  database: 'odooTecsup',
  username: 'rosario.huanca@tecsup.edu.pe',
  password: 'root123'
});

// Connección a Odoo 
odoo.connect(function (err) {
  if (err) { return console.log(err); }
  console.log("entro");
})

//Clase App que extiende de React.Component
export default class App extends React.Component {
  //constructor de un componente React
  constructor(props) {
    super(props);
    //state es el estado del componente
    this.state = {
      partners: [{name:'xxx'}]
    }
  }
  //componente se montó
  componentDidMount() {
    odoo.get('convalidaciones.alumno',{
      ids: [1,2,3,4,5,29],
      fields: [ 'name' ],
    },function(err,partners){
      console.log(partners);
      //cambiamos el estado a los partners del Odoo
      this.setState({
        partners: partners
      })
      //bind es como indicar self o this
    }.bind(this))
  }
  //función principal y se encarga de actualizar la vista
  render() {
    return (
      <View style={styles.container}>
        <FlatList
          data={this.state.partners}
          //renderizamos cada item en text
          renderItem={({item}) => <Text>{item.name}</Text>}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
