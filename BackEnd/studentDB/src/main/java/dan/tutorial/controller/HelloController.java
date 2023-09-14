package dan.tutorial.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;



@RestController
public class HelloController {

    @RequestMapping(value = "/helloworld1",method = RequestMethod.GET)
    public String helloWorld1(){
        return "Hello, world!";
    }
    @GetMapping("/helloworld2")
    public String helloWorld(){
        return "Hello, world!";
    }
} 
