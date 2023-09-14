package dan.tutorial.entity;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.NotBlank;

import javax.persistence.*;
import javax.validation.constraints.Future;
import javax.validation.constraints.FutureOrPresent;
import javax.validation.constraints.Negative;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder

public class Department {
    
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long departmentId;
    @NotBlank(message ="Please Add Department Name")
    //@Length(min = 1, max=255)
    //@Size(min =1, max = 255)
    //@EmailAddress(message = "Please Add A Valid Email")
    //@Positive
    //@Negative
    //@FutureOrPresent


    private String departmentName;
    private String departmentAddress;
    private String departmentCode;

}
