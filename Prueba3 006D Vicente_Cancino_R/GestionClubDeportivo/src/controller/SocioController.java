/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;


import bd.Conexion;
import java.util.ArrayList;
import java.util.List;
import models.Socio; 

import java.sql.ResultSet;
import java.sql.PreparedStatement;
import java.sql.Statement;
 

public class SocioController {
    Conexion cx;
    HelperController helper = new HelperController();
    public SocioController(){
        cx = new Conexion();
        cx.conectar();
    }

    
    public List<Socio> obtenerSocio (int rut){
        List <Socio> socios = new ArrayList<>();
        String query = "SELECT * FROM LIBRO WHERE rut" + rut + ";";
        try{
            ResultSet rs = cx.EjecutarQuery(query);
            while (rs.next()){
                socios.add(new Socio(rs.getInt("rut"), rs.getString("nombre"), rs.getString("fecha_nac"), rs.getString("direccion"), rs.getBoolean("memb_activa")));
            }
        }catch(Exception e){
            System.out.println("Error");
        }
        return socios;
    }

    public Socio BuscarSocioPorRut(int rut){
        Socio socioEncontrado = null;
        String query = "SELECT * FROM SOCIO WHERE RUT =" + rut + ";";
        try{
            ResultSet rs = cx.EjecutarQuery(query);
            if(rs.next()){
                socioEncontrado = new Socio();
                socioEncontrado.setRut(rs.getInt("rut"));
                socioEncontrado.setNombre(rs.getString("nombre"));
                socioEncontrado.setFecha_nac(rs.getString("fecha_nac"));
                socioEncontrado.setDireccion(rs.getString("direccion"));
                socioEncontrado.setMemb_activa(rs.getBoolean("memb_activa"));
            }
        }catch(Exception e){
            System.out.println("Error");
        }
        return socioEncontrado;
    }
    
    public void editarSocio(int rut, String nombre, String fecha_nac, String direccion, Boolean memb_activa){
        String query = "UPDATE SOCIO setNombre=" + nombre + "fecha_nac" + fecha_nac + "direccion" + direccion + "memb_activa" + memb_activa + "WHERE rut" + rut + ";";
        System.out.println(query);
        try{
        Socio socioEncontrado = BuscarSocioPorRut(rut);
            if(socioEncontrado != null){
            Statement st = cx.getConnection().createStatement();
            st.executeUpdate(query);
            helper.showInformation("Socio actualizado");
            }else {
                helper.showInformation("El socio no se encontro");
            } 
        }catch(Exception e){
            System.out.println("Error");
        }
    }
    
    public void eliminarSocio(int rut){
        String query = "DELETE FROM SOCIO WHERE rut =" + rut + ";";
        try{
        Socio socioEncontrado = BuscarSocioPorRut(rut);
            if (socioEncontrado != null){
                Statement st = cx.getConnection().createStatement();
                st.executeUpdate(query);
                System.out.println("Se elimino el Socio");
            }else {
                helper.showInformation("El socio no se encontro");
            }
        }catch(Exception e){
            System.out.println("Error");
        }
    }
}