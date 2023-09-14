package com.project.TheGallery.repository;

import com.project.TheGallery.entity.Artist;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ArtistRepository extends JpaRepository<Artist,Integer> {
    //Custom Queries!

    @Query(value="SELECT * FROM artists.gallerytable AS GT ORDER BY RAND() LIMIT 1",nativeQuery=true)
    public Artist findArtistRandom();

    @Query(value="SELECT * FROM artists.gallerytable AS GT ORDER BY RAND() LIMIT ?1 ",nativeQuery=true)
    public List<Artist> findArtistRandomList(Integer artistCount);

    @Query(value="SELECT * FROM artists.gallerytable AS GT ORDER BY RAND() LIMIT 10",nativeQuery=true)
    public List<Artist> findArtistRandom10();

    @Query(value="SELECT * FROM artists.gallerytable WHERE name = ?1 LIMIT 1",nativeQuery=true)
    public Artist findArtistByName(String artistName);


}
